import pandas as pd
import streamlit as st

REQUIRED_COLUMNS = {
    "HS Code": ["HS Code", "HS_CODE"],
    "Product Description": ["Product Description", "Description"],
    "Quantity": ["Quantity", "Qty"],
    "Unit": ["Unit"],
    "Unit Price (USD)": ["Unit Price (USD)", "Unit Price"],
    "CIF Value (USD)": ["CIF Value (USD)", "Value (USD)"],
    "Importer Name": ["Importer Name", "Importer"],
    "Supplier Name": ["Supplier Name", "Supplier"],
    "Foreign Country": ["Foreign Country", "Country"],
    "Date": ["Date"]
}

def load_and_clean_data(file):
    df = pd.read_excel(file)
    df.columns = df.columns.str.strip()
    
    # Try to rename columns to standard names
    col_map = {}
    for std_name, options in REQUIRED_COLUMNS.items():
        for opt in options:
            if opt in df.columns:
                col_map[opt] = std_name
                break

    df.rename(columns=col_map, inplace=True)

    # Notify missing columns
    missing_cols = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing_cols:
        st.warning(f"Missing columns in file: {', '.join(missing_cols)}")

    # Clean known fields
    if "CIF Value (USD)" in df.columns:
        df["CIF Value (USD)"] = pd.to_numeric(df["CIF Value (USD)"], errors='coerce')
    if "Quantity" in df.columns:
        df["Quantity"] = pd.to_numeric(df["Quantity"], errors='coerce')
    if "Unit Price (USD)" in df.columns:
        df["Unit Price (USD)"] = pd.to_numeric(df["Unit Price (USD)"], errors='coerce')
    if "Product Description" in df.columns:
        df["Product Description"] = df["Product Description"].astype(str).str.strip().str.upper()

    df.dropna(how='all', inplace=True)
    return df
