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
├── data/                 # Raw and processed datasets
├── notebooks/            # Jupyter notebooks for experimentation
├── models/               # Trained LSTM and BiLSTM models
├── pipeline/             # Dagster and Spark pipeline scripts
├── app/                  # Streamlit visualization app
├── utils/                # Helper functions
└── README.md             # Project documentation
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
