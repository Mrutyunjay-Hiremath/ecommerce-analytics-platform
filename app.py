import streamlit as st
import duckdb
import pandas as pd
import plotly.express as px

# 1. Page Configuration
st.set_page_config(page_title="Executive Analytics", layout="wide")

# 2. Custom CSS for Dark Mode & Polish
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FAFAFA; }
    .kpi-card { 
        background-color: #262730; 
        padding: 20px; 
        border-radius: 10px; 
        text-align: center; 
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }
    </style>
""", unsafe_allow_html=True)

# 3. Data Loading
@st.cache_data(ttl=60)
def load_data():
    conn = duckdb.connect("data/analytics.db")
    df = conn.execute("SELECT * FROM transactions").df()
    conn.close()
    return df

df = load_data()

# 4. Dashboard Header
st.title("📊 E-Commerce Analytics Platform")
st.markdown("---")

# 5. KPI Metrics
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f"<div class='kpi-card'><h3>Total Revenue</h3><h2>${df['Amount'].sum():,.2f}</h2></div>", unsafe_allow_html=True)
with col2:
    st.markdown(f"<div class='kpi-card'><h3>Total Orders</h3><h2>{len(df):,}</h2></div>", unsafe_allow_html=True)
with col3:
    churn_rate = (df['Churned'].mean()) * 100
    st.markdown(f"<div class='kpi-card'><h3>Churn Rate</h3><h2>{churn_rate:.1f}%</h2></div>", unsafe_allow_html=True)

st.markdown("---")

# 6. Visualizations
st.markdown("### Revenue by Product Category")
fig = px.bar(
    df.groupby('ProductCategory')['Amount'].sum().reset_index(), 
    x='ProductCategory', 
    y='Amount', 
    color='ProductCategory',
    template="plotly_dark"
)
st.plotly_chart(fig, use_container_width=True)