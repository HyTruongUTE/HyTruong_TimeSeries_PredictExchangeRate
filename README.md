# HyTruong_TimeSeries_PredictExchangeRate

## 📊 Project Overview

**HyTruong_TimeSeries_PredictExchangeRate** is a project focused on forecasting the **VND/USD exchange rate** using deep learning models **LSTM** and **BiLSTM**. The project aims to analyze historical data and predict short-term exchange rate trends to support financial decision-making.

## 🚀 Features

* **Automated Data Crawling**: Real-time exchange rate data automatically collected from **Vietcombank**.
* **Modern Data Architecture**: Built on a **Data Lakehouse** using **Apache Spark** for data processing and **Dagster** for data pipeline orchestration.
* **Deep Learning Models**: Implementation of **LSTM** and **BiLSTM** architectures with different optimization techniques (Adam, RMSProp, SGD).
* **Flexible Data Splitting**: Supports multiple train-test ratios (60-40, 70-30, 80-20, 90-10).
* **Custom Input Structures**: Experiments with different time window structures (7in1out, 14in2out, etc.).
* **Interactive Visualization**: Prediction results displayed via a **Streamlit dashboard** for intuitive data exploration.

## 🧠 Tech Stack

* **Languages**: Python
* **Frameworks & Libraries**: TensorFlow, Keras, Pandas, NumPy, Matplotlib
* **Data Pipeline**: Apache Spark, Dagster
* **Visualization**: Streamlit
* **Data Source**: Vietcombank (Exchange Rate API)

## ⚙️ Project Structure

```
HyTruong_TimeSeries_PredictExchangeRate/
├── app.py
├── crawler.py
├── chromedriver-win64/
│   ├── chromedriver.exe
│   ├── LICENSE.chromedriver
│   └── THIRD_PARTY_NOTICES.chromedriver
│
├── DPRE/
│   ├── data_clean/
│   │   ├── aud_rates.csv
│   │   ├── euro_rates.csv
│   │   ├── gbp_rates.csv
│   │   ├── jpy_rates.csv
│   │   └── usd_rates.csv
│   ├── data_preprocessing.ipynb
│   └── vietnam_exchange_rate.csv
│
├── minio/
│   ├── aud/
│   │   ├── aud_rates.snappy.parquet
│   │   └── part-00000-37f4c5e9-b2d8-4358-9c7c-eb662730f257-c000.snappy.parquet
│   ├── euro/
│   │   ├── euro_rates.snappy.parquet
│   │   └── part-00000-12bff8a7-5eca-45d1-9c4d-76bcbd3b8261-c000.snappy.parquet
│   ├── gbp/
│   │   ├── gbp_rates.snappy.parquet
│   │   └── part-00000-dc91c846-03af-491a-992d-2b0e8b7175ea-c000.snappy.parquet
│   ├── jpy/
│   │   ├── jpy_rates.snappy.parquet
│   │   └── part-00000-4990b459-45c5-4e82-92c2-59655a001a75-c000.snappy.parquet
│   └── usd/
│       ├── usd_rates.snappy.parquet
│       └── part-00000-18b834c3-cd6d-42ae-82c3-638999ff6d84-c000.snappy.parquet
│
├── Model/
│   ├── case_1/
│   │   ├── BiLSTM/
│   │   │   ├── model_ADAM/
│   │   │   │   ├── predict.csv
│   │   │   │   ├── save_model.hdf5
│   │   │   │   └── scaler.save
│   │   │   ├── model_RMSPROP/
│   │   │   │   ├── predict.csv
│   │   │   │   └── save_model.hdf5
│   │   │   └── model_SGD/
│   │   │       ├── predict.csv
│   │   │       └── save_model.hdf5
│   │   └── LSTM/
│   │       ├── model_ADAM/
│   │       │   ├── predict.csv
│   │       │   └── save_model.hdf5
│   │       ├── model_RMSPROP/
│   │       │   ├── predict.csv
│   │       │   └── save_model.hdf5
│   │       └── model_SGD/
│   │           ├── predict.csv
│   │           └── save_model.hdf5
│   │
│   ├── case_2/
│   │   ├── BiLSTM/
│   │   │   ├── model_6040/
│   │   │   │   ├── predict.csv
│   │   │   │   └── save_model.hdf5
│   │   │   ├── model_7030/
│   │   │   │   ├── predict.csv
│   │   │   │   └── save_model.hdf5
│   │   │   ├── model_8020/
│   │   │   │   ├── predict.csv
│   │   │   │   └── save_model.hdf5
│   │   │   └── model_9010/
│   │   │       ├── predict.csv
│   │   │       └── save_model.hdf5
│   │   └── LSTM/
│   │       ├── model_6040/
│   │       │   ├── predict.csv
│   │       │   └── save_model.hdf5
│   │       ├── model_7030/
│   │       │   ├── predict.csv
│   │       │   └── save_model.hdf5
│   │       ├── model_8020/
│   │       │   ├── predict.csv
│   │       │   └── save_model.hdf5
│   │       └── model_9010/
│   │           ├── predict.csv
│   │           └── save_model.hdf5
│   │
│   └── case_3/
│       ├── BiLSTM/
│       │   ├── model_7in1out/
│       │   │   ├── predict.csv
│       │   │   └── save_model.hdf5
│       │   └── model_14in2out/
│       │       ├── predict.csv
│       │       └── save_model.hdf5
│       └── LSTM/
│           ├── model_7in1out/
│           │   ├── predict.csv
│           │   └── save_model.hdf5
│           └── model_14in2out/
│               ├── predict.csv
│               └── save_model.hdf5
│
├── __pycache__/
│   └── crawler.cpython-39.pyc
│
├── Case1_BiLSTM_ADAM.ipynb
├── Case1_BiLSTM_RMSPROP.ipynb
├── Case1_BiLSTM_SGD.ipynb
├── Case1_LSTM_ADAM.ipynb
├── Case1_LSTM_RMSPROP.ipynb
├── Case1_LSTM_SGD.ipynb
├── Case2_BiLSTM_6040.ipynb
├── Case2_BiLSTM_7030.ipynb
├── Case2_BiLSTM_8020.ipynb
├── Case2_BiLSTM_9010.ipynb
├── Case2_LSTM_6040.ipynb
├── Case2_LSTM_7030.ipynb
├── Case2_LSTM_8020.ipynb
├── Case2_LSTM_9010.ipynb
├── Case3_BiLSTM_7in1out.ipynb
├── Case3_BiLSTM_14in2out.ipynb
├── Case3_LSTM_7in1out.ipynb
└── Case3_LSTM_14in2out.ipynb

```

## 📈 Results

* LSTM and BiLSTM models demonstrate high accuracy in capturing exchange rate trends.
* The **BiLSTM model** provides smoother and more stable predictions due to its bidirectional learning capability.

## 🔮 Future Improvements

* Incorporate macroeconomic indicators (inflation, interest rates, etc.) for multivariate forecasting.
* Deploy the model via a cloud-based API for real-time predictions.
* Integrate dashboard with automated model retraining pipeline.

## 👨‍💻 Author

**Hy Truong** – IT Engineering From **Ho Chi Minh City University of Technology and Education (HCMUTE)**, specializing in **Information Systems**.

## 📬 Contact

* **Email:** [truongledanhy589069@gmail.com](mailto:truongledanhy589069@gmail.com)
* **LinkedIn:** [[linkedin.com/in/hytruong](https://www.linkedin.com/in/truong-le-dan-hy-b2820424b/)](#)

---

⭐ *If you find this project helpful, feel free to star the repository and share your feedback!*
