import streamlit as st
import pandas as pd
from data_loader import load_and_clean_data
from aggregator import aggregate_data
from query_engine import apply_query
from visuals import generate_charts
from utils import download_excel

st.set_page_config(page_title="IGBT Trade Dashboard", layout="wide")
st.title("📊 Trade Data Dashboard")

uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx"])

if uploaded_file:
    df = load_and_clean_data(uploaded_file)

    st.subheader("✅ Raw Data")
    st.dataframe(df)

    agg_df = aggregate_data(df)

    st.subheader("📦 Aggregated Data (Grouped by Product)")
    st.dataframe(agg_df)

    st.subheader("🔎 Query Filters")
    filtered_df = apply_query(df)

    st.subheader("📊 Visualizations")
    generate_charts(filtered_df)

    st.download_button("Download Aggregated Data as Excel",
                       data=download_excel(agg_df),
                       file_name="aggregated_trade_data.xlsx",
                       mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
