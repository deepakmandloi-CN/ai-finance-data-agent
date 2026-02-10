import pandas as pd
import os

DATA_PATH = os.path.join("data", "finance_raw_data_10000_rows.csv")

def load_data():
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(f"Data file not found at {DATA_PATH}")

    df = pd.read_csv(DATA_PATH)
    df["transaction_date"] = pd.to_datetime(df["transaction_date"])
    return df
