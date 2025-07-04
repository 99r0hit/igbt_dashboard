import pandas as pd
import streamlit as st

def aggregate_data(df):
    grouped = df.groupby('Product Description').agg({
        'Quantity': 'sum',
        'CIF Value (USD)': 'sum',
        'Unit Price (USD)': 'mean'
    }).reset_index()
    grouped.sort_values(by='CIF Value (USD)', ascending=False, inplace=True)
    return grouped
