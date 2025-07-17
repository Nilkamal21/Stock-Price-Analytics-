import pandas as pd

def clean_stock_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna()
    df['Datetime'] = pd.to_datetime(df['Datetime'])
    df = df.sort_values(by='Datetime')
    df.reset_index(drop=True, inplace=True )
    return df

def resample_to_hourly(df: pd.DataFrame)-> pd.DataFrame:
    df.set_index('Datetime',inplace=True)
    df_hourly = df.resample('1h').agg({
        'Open': 'first',
        'High': 'max',
        'Low': 'min',
        'Close': 'last',
        'Volume': 'sum',
        'Ticker': 'last'
    }).dropna().reset_index()
    return df_hourly

def add_moving_average(df: pd.DataFrame, window: int = 3) -> pd.DataFrame:
    df[f'MA_{window}'] = df['Close'].rolling(window=window).mean()
    return df

def clean_and_transform_data(df: pd.DataFrame) -> pd.DataFrame:
    df = clean_stock_data(df)
    df = resample_to_hourly(df)
    df = add_moving_average(df)
    return df
