import pandas as pd
from sqlalchemy import create_engine

def load_to_sqlite(df , db_name="stock_data.db",table_name="stock_hourly"):
    engine = create_engine(f"sqlite:///{db_name}",echo=False)
    df.to_sql(table_name, con=engine, if_exists="replace" , index=False)
    print(f"✅ Data loaded into table '{table_name}' in DB '{db_name}' successfully!")