# 📊 End-to-End E-Commerce Analytics Platform

## Overview
An automated Business Intelligence and Analytics platform built entirely in Python. This application ingests raw transactional data, processes it through an automated ETL pipeline, stores it in a high-performance database, and serves actionable business KPIs and Machine Learning predictions via an interactive web dashboard.

## 🏗️ Architecture & Tech Stack
* **Data Engine & ETL:** Pandas, DuckDB
* **Machine Learning:** Scikit-learn (Random Forest Classifier for Churn Prediction)
* **Frontend UI:** Streamlit, Plotly, Custom CSS
* **Language:** Python 3.x
* **Automation:** GitHub Actions (CI/CD Pipeline)

```mermaid
graph TD
    %% Custom Colors
    classDef automation fill:#2ea44f,stroke:#22863a,stroke-width:2px,color:#fff;
    classDef python fill:#3776AB,stroke:#2b5b84,stroke-width:2px,color:#fff;
    classDef db fill:#F6D155,stroke:#b39b3b,stroke-width:2px,color:#333;
    classDef ml fill:#FF9900,stroke:#cc7a00,stroke-width:2px,color:#fff;
    classDef ui fill:#FF4B4B,stroke:#cc3c3c,stroke-width:2px,color:#fff;

    A[🕒 GitHub Actions<br/>Daily Automation]:::automation -->|Triggers| B(🐍 Data Generator<br/>Simulates Sales):::python
    B -->|Raw Data CSV| C(🧹 Pandas ETL<br/>Clean & Transform):::python
    C -->|Processed Data| D[(🦆 DuckDB<br/>Analytics Engine)]:::db
    D -->|Feature Data| E{{🤖 Scikit-Learn<br/>Churn Predictor}}:::ml
    E -->|Model Validation| D
    D -->|Query KPIs| F[📊 Streamlit<br/>Live Web Dashboard]:::ui
