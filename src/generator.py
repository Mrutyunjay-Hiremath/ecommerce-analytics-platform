import numpy as np
import pandas as pd

np.random.seed(42)
n_rows = 5000

data = {
    "TransactionID": [f"TXN-{10000 + i}" for i in range(n_rows)],
    "CustomerID": np.random.choice(
        [f"CUST-{np.random.randint(100, 999)}" for _ in range(300)], n_rows
    ),
    "TransactionDate": pd.date_range(
        start="2023-01-01", periods=n_rows, freq="h"
    ).astype(str),
    "ProductCategory": np.random.choice(
        ["Electronics", "Clothing", "Home & Kitchen", "Beauty", "Books"], n_rows
    ),
    "Amount": np.random.normal(loc=120, scale=40, size=n_rows).round(2),
    "PaymentMethod": np.random.choice(
        ["Credit Card", "PayPal", "UPI", "Debit Card"], n_rows
    ),
    "CustomerAge": np.random.choice([18, 25, 34, 45, 52, 60, np.nan], n_rows),
    "Churned": np.random.choice([0, 1], n_rows, p=[0.75, 0.25]),
}

df = pd.DataFrame(data)
# Introduce duplicate entries & realistic messy data
df = pd.concat([df, df.iloc[:50]], ignore_index=True)
df.to_csv("data/raw_data.csv", index=False)
print("Raw enterprise dataset generated successfully in 'data/raw_data.csv'")