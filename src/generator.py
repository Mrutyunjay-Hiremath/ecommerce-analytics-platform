import numpy as np
import pandas as pd
import os
from datetime import datetime

def generate_daily_data():
    file_path = "data/raw_data.csv"
    
    # Generate a random amount of new daily transactions
    nrows = np.random.randint(50, 150)

    data = {
        "TransactionID": [f"TXN-{np.random.randint(100000, 999999)}" for _ in range(nrows)],
        "CustomerID": np.random.choice([f"CUST-{np.random.randint(100, 999)}" for _ in range(300)], nrows),
        "TransactionDate": [datetime.now().strftime("%Y-%m-%d %H:%M:%S") for _ in range(nrows)],
        "ProductCategory": np.random.choice(["Electronics", "Clothing", "Home & Kitchen", "Beauty", "Books"], nrows),
        "Amount": np.random.normal(loc=120, scale=40, size=nrows).round(2),
        "PaymentMethod": np.random.choice(["Credit Card", "PayPal", "UPI", "Debit Card"], nrows),
        "CustomerAge": np.random.choice([18, 25, 34, 45, 52, 60, np.nan], nrows),
        "Churned": np.random.choice([0, 1], nrows, p=[0.75, 0.25])
    }

    new_df = pd.DataFrame(data)

    # Append to existing data if it exists
    if os.path.exists(file_path):
        existing_df = pd.read_csv(file_path)
        updated_df = pd.concat([existing_df, new_df], ignore_index=True)
    else:
        updated_df = new_df

    updated_df.to_csv(file_path, index=False)
    print(f"Added {nrows} new daily transactions. Total records: {len(updated_df)}")

if __name__ == "__main__":
    generate_daily_data()