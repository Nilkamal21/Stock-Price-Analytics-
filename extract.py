import yfinance as yf
import pandas as pd
# === Function to fetch stock data ===
def fetch_stock_data(ticker='AAPL', interval='1d', period='1mo'):
    df = yf.download(tickers=ticker, interval=interval, period=period, progress=False, auto_adjust=False)

    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    df.reset_index(inplace=True)
    df['Ticker'] = ticker

    if 'Adj Close' not in df.columns and 'Close' in df.columns:
        df['Adj Close'] = df['Close']

    return df

