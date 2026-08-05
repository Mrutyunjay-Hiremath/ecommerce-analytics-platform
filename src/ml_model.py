import duckdb
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

def train_model():
    # 1. Connect to DB and fetch data
    conn = duckdb.connect("data/analytics.db")
    df = conn.execute("SELECT Amount, CustomerAge, Churned FROM transactions").df()
    conn.close()

    # 2. Prepare features (X) and target (y)
    X = df[["Amount", "CustomerAge"]]
    y = df["Churned"]

    # 3. Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 4. Train Model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # 5. Evaluate and Save
    preds = model.predict(X_test)
    print(f"Model Accuracy: {accuracy_score(y_test, preds):.2f}")
    
    # Save the model to disk
    joblib.dump(model, "data/churn_model.pkl")
    print("Model saved successfully to 'data/churn_model.pkl'")

if __name__ == "__main__":
    train_model()