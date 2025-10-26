import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
import numpy as np
import os
import matplotlib.pyplot as plt
from datetime import datetime
from crawler import crawl_exchange_rates 
import os

DATA_FOLDER = "./minio"
MODEL_FOLDER = ".\Model"


@st.cache_data
def load_exchange_data(currency):
    filepath = os.path.join(DATA_FOLDER, currency.lower(),f"{currency.lower()}_rates.snappy.parquet")
    df = pd.read_parquet(filepath, engine="pyarrow")
    df['ngay'] = pd.to_datetime(df['ngay'])
    return df

def prepare_input(df, n_steps=7):
    seq = df['mua_chuyen_khoan'].values[-n_steps:]
    seq_reshaped = seq.reshape(1, n_steps, 1)
    return seq, seq_reshaped

# SIDEBAR 
page = st.sidebar.radio("Chọn chức năng", ["📈Cào dữ liệu","📊Xem tập dữ liệu", "📈Mô hình dự báo","🏚️ Home"])

# PAGE 1
if page == "📈Cào dữ liệu":
    st.title("📊 Khám phá dữ liệu tỷ giá hối đoái")
    # Thêm thanh sidebar cho chức năng khác
    st.sidebar.title("Chức năng")

    # Các lựa chọn trong sidebar
    sidebar_option = st.sidebar.selectbox("Chọn chức năng", ["Crawl Dữ Liệu"])
    # Xử lý chức năng theo lựa chọn trong sidebar
    if sidebar_option == "Crawl Dữ Liệu":
        st.title('Crawl Tỷ Giá Ngoại Tệ Từ Vietcombank')
        start_date_input = st.date_input("Chọn ngày bắt đầu", datetime(2025, 1, 1))
        end_date_input = st.date_input("Chọn ngày kết thúc", datetime.today())
        result_df = None

        if st.button('Crawl Dữ Liệu'):
            start_date = datetime.strptime(str(start_date_input), "%Y-%m-%d")
            end_date = datetime.strptime(str(end_date_input), "%Y-%m-%d")
            
            st.write(f"Đang lấy dữ liệu từ {start_date.strftime('%d/%m/%Y')} đến {end_date.strftime('%d/%m/%Y')}...")
            result_df = crawl_exchange_rates(start_date, end_date)
            
            if result_df is not None:
                st.success("Dữ liệu đã được lấy thành công!")
                st.dataframe(result_df)  
                
                file_name = f"exchange_rate_{start_date.strftime('%d%m%Y')}_{end_date.strftime('%d%m%Y')}.csv"
                file_path = os.path.join(os.getcwd(), file_name)
                
                result_df.to_csv(file_path, index=False, encoding='utf-8')
                
                with open(file_path, 'rb') as f:
                    st.download_button(
                        label="Lưu dữ liệu",
                        data=f,
                        file_name=file_name,
                        mime="text/csv"
                    )
            else:
                st.error("Không có dữ liệu nào được lấy!")
            

# PAGE 2
elif page == "📊Xem tập dữ liệu":
    st.title("📊 Khám phá dữ liệu tỷ giá hối đoái")

    # Chọn loại tiền
    currency = st.sidebar.selectbox("Chọn loại tiền tệ", ['usd', 'euro', 'aud', 'gbp', 'jpy'])
    df = load_exchange_data(currency)

    # Y mode
    scale_mode = st.sidebar.selectbox("Chuẩn hóa dữ liệu", ["Toàn bộ"])

    if scale_mode == "Toàn bộ":
        ymin, ymax = df['mua_chuyen_khoan'].min(), df['mua_chuyen_khoan'].max()
    elif scale_mode == "Tự động (90%)":
        ymin = df['mua_chuyen_khoan'].quantile(0.05)
        ymax = df['mua_chuyen_khoan'].quantile(0.95)
    elif scale_mode == "Tự động (Mean ± 2σ)":
        mean = df['mua_chuyen_khoan'].mean()
        std = df['mua_chuyen_khoan'].std()
        ymin = mean - 2 * std
        ymax = mean + 2 * std


    start_date = df['ngay'].min().strftime('%d/%m/%Y')
    end_date = df['ngay'].max().strftime('%d/%m/%Y')

    # Hiển thị biểu đồ
    st.subheader(f"Tỷ giá {currency.upper()}/VND từ {start_date} đến {end_date}")

    # Tạo biểu đồ với Altair
    import altair as alt
    chart = alt.Chart(df).mark_line(color='steelblue').encode(
        x=alt.X('ngay:T', title='Thời gian'),
        y=alt.Y('mua_chuyen_khoan:Q', title='Tỷ giá mua chuyển khoản (VND)', scale=alt.Scale(domain=[ymin, ymax])),
        tooltip=[
            alt.Tooltip('ngay:T', title='Thời gian'),
            alt.Tooltip('mua_chuyen_khoan:Q', title='Tỷ giá')
        ]
    ).properties(
        width=800,
        height=400,
        title=f"Biểu đồ tỷ giá {currency.upper()}/VND"
    ).interactive()

    st.altair_chart(chart, use_container_width=True)
    

# PAGE 3
elif page == "📈Mô hình dự báo":
    st.title("📈 Dự báo tỷ giá USD/VND bằng mô hình LSTM và BiLSTM")

    currency = st.sidebar.selectbox("Tỷ giá hối đoái", ['usd'])
    df = load_exchange_data(currency)

    st.sidebar.markdown("---")
    st.sidebar.subheader("Chọn mô hình")

    case = st.sidebar.selectbox("Chọn trường hợp: ", ['case_1', 'case_2', 'case_3'])
    model_type = st.sidebar.selectbox("Chọn mô hình: ", ['LSTM', 'BiLSTM'])

    model_dir = os.path.join(MODEL_FOLDER, case, model_type)
    predict_choices = []
    for root, dirs, files in os.walk(model_dir):
        for file in files:
            if file.endswith('.csv'):
                rel_path = os.path.relpath(os.path.join(root, file), MODEL_FOLDER)
                predict_choices.append(rel_path)

    selected_model_path = st.sidebar.selectbox("Chọn tập dự báo", predict_choices)
    
    full_predict_path = os.path.join(MODEL_FOLDER, selected_model_path)

    st.markdown(f"**Đường dẫn file dự báo:** `{full_predict_path}`")


    # Đọc file CSV kết quả dự báo
    try:
        predict_df = pd.read_csv(full_predict_path)
        
        from sklearn.metrics import mean_absolute_error, mean_squared_error
        mae = mean_absolute_error(predict_df['Giá thực tế'], predict_df['Giá dự đoán'])
        mse = mean_squared_error(predict_df['Giá thực tế'], predict_df['Giá dự đoán'], squared=True)  # MSE
        rmse = mean_squared_error(predict_df['Giá thực tế'], predict_df['Giá dự đoán'], squared=False)  # RMSE

        # Hiển thị metric
        col1, col2, col3 = st.columns(3)
        col1.metric("📉 MAE", f"{mae:.3f}")
        col2.metric("📉 MSE", f"{mse:.3f}")
        col3.metric("📉 RMSE", f"{rmse:.3f}")

        st.subheader("📄 Kết quả dự báo")
        st.dataframe(predict_df[['Giá thực tế', 'Giá dự đoán']].reset_index(drop=True), use_container_width=True)

    except Exception as e:
        st.error(f"Không thể đọc file dự báo. Lỗi: {e}")
        
# PAGE 4
elif page == "🏚️ Home":
    st.markdown("""
    <meta http-equiv="refresh" content="0; url=http://localhost:8501">
""", unsafe_allow_html=True)
