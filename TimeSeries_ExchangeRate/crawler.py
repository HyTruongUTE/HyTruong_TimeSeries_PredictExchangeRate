# crawler.py
import pandas as pd
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
from io import StringIO
import os

# Hàm crawl data
def crawl_exchange_rates(start_date, end_date):
    # Khởi tạo trình duyệt
    chromedriver_path = './chromedriver-win64/chromedriver.exe'
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service)
    options = Options()
    options.add_argument("--headless") 
    wait = WebDriverWait(driver, 10)
    # Truy cập trang tỷ giá Vietcombank
    url = 'https://www.vietcombank.com.vn/vi-VN/KHCN/Cong-cu-Tien-ich/Ty-gia'
    driver.get(url)

    # Chờ trang tải xong
    time.sleep(2)
    
    # Khởi tạo danh sách lưu dữ liệu
    all_data = []

    # Lặp qua từng ngày trong khoảng thời gian
    current_date = start_date
    while current_date <= end_date:
        date_str = current_date.strftime('%d%m%Y')
        try:
            date_picker = wait.until(EC.element_to_be_clickable((By.ID, 'datePicker')))
            driver.execute_script("arguments[0].click();", date_picker)
            date_picker.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
            date_picker.send_keys(date_str)
            
            time.sleep(2)

            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "table-wrapper")))

            table_html = driver.find_element(By.CLASS_NAME, "table-wrapper").get_attribute('outerHTML')
            table_html_io = StringIO(table_html)
            df = pd.read_html(table_html_io)[0]
            df.insert(0, 'Ngày', current_date.strftime('%d/%m/%Y'))
            # Xử lý dữ liệu sau khi đọc
            df.columns = ['ngay', 'ma_ngoai_te', 'ten_ngoai_te', 'mua_tien_mat', 'mua_chuyen_khoan', 'ban']
            all_data.append(df)
        except Exception as e:
            print(f"Lỗi khi lấy dữ liệu ngày {current_date.strftime('%Y-%m-%d')}: {e}")
        
        current_date += timedelta(days=1)
    
    driver.quit()

    # Kiểm tra xem có dữ liệu không
    if all_data:
        final_df = pd.concat(all_data, ignore_index=True)
        print(f"Dữ liệu đã crawl thành công với {len(final_df)} dòng dữ liệu.")
        return final_df
    else:
        print("Không có dữ liệu crawl được.")
        return None

# Hàm lưu dữ liệu vào file CSV
def save_to_csv(df, start_date, end_date):
    if df is not None:
        # Đảm bảo thư mục ./data tồn tại
        if not os.path.exists('./data'):
            print("Thư mục ./data không tồn tại, sẽ tạo mới.")
            os.makedirs('./data')
        else:
            print("Thư mục ./data đã tồn tại.")

        # Tạo tên file theo định dạng "exchange_rate_ngaybatdau_ngayketthuc.csv"
        file_name = f"exchange_rate_{start_date.strftime('%d%m%Y')}_{end_date.strftime('%d%m%Y')}.csv"
        file_path = os.path.join('./data', file_name)

        # In đường dẫn để kiểm tra
        print(f"Đường dẫn file sẽ lưu: {file_path}")

        # Lưu DataFrame vào file CSV
        df.to_csv(file_path, index=False, encoding='utf-8')
        return file_path
    else:
        print("Không có dữ liệu để lưu!")
        return None
