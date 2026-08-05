import duckdb
import pandas as pd


def run_etl():
    # 1. Load Data
    df = pd.read_csv("data/raw_data.csv")

    # 2. Clean Data
    df = df.drop_duplicates(subset=["TransactionID"])
    df["TransactionDate"] = pd.to_datetime(df["TransactionDate"])
    df["Amount"] = df["Amount"].apply(lambda x: max(x, 5.00))  # Fix anomalies
    df["CustomerAge"] = df["CustomerAge"].fillna(
        df["CustomerAge"].median()
    )  # Impute missing values

    # 3. Store into High-Performance DuckDB Database
    conn = duckdb.connect("data/analytics.db")
    conn.execute(
        "CREATE OR REPLACE TABLE transactions AS SELECT * FROM df"
    )
    conn.close()

    print("ETL Pipeline complete. Data persisted to DuckDB ('data/analytics.db').")


if __name__ == "__main__":
    run_etl()