# 📈 Stock Price Analytics Dashboard

An interactive and visually appealing stock price analytics dashboard built using **Dash**, **Plotly**, and **YFinance**. It enables users to analyze historical stock data, visualize line and candlestick charts, and explore the top 10 global companies — all in a sleek, web-based interface.

🔗 **Live Demo**: [https://stock-price-analytics-1.onrender.com](https://stock-price-analytics-1.onrender.com)

---

## 🚀 Features

- 📊 **Line & Candlestick Charts** for selected stocks  
- 🔍 **Top 10 Companies Dropdown** and custom symbol input  
- ⏳ **Selectable Date Ranges** and time intervals  
- 📁 Modular ETL architecture (`extract.py`, `transform.py`, `load.py`)  
- 💬 Friendly user prompts and error handling  

---

## 📂 Project Structure

```
stock-etl-dashboard/
│
├── dashboard.py         # Main Dash application
├── extract.py           # Stock data extraction using yfinance
├── transform.py         # Data transformation logic
├── load.py              # Data loading or processing logic
├── requirements.txt     # Python dependencies
├── render.yaml          # Render deployment configuration
└── README.md            # Project documentation
```

---

## 📦 Installation

1. **Clone the repository**
```bash
git clone https://github.com/Nilkamal21/Stock-Price-Analytics.git
cd Stock-Price-Analytics
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the app locally**
```bash
python dashboard.py
```

The app will be available at: `http://127.0.0.1:8050`

---

## 🌐 Deployment on Render

This app is deployed on [Render](https://render.com).

### 🔧 Deployment Configuration

- **Start Command:** `python dashboard.py`  
- **Build Command:** `pip install -r requirements.txt`  
- **Port:** `8080`  
- **Hosted Link:** [https://stock-price-analytics-1.onrender.com](https://stock-price-analytics-1.onrender.com)

---

## 💡 Technologies Used

- [Dash](https://dash.plotly.com/)
- [Plotly](https://plotly.com/python/)
- [YFinance](https://pypi.org/project/yfinance/)
- [Pandas](https://pandas.pydata.org/)
- [Render](https://render.com/) for deployment

---
