import streamlit as st

def apply_query(df):
    if "HS Code" in df.columns:
        hs_codes = df["HS Code"].dropna().unique().tolist()
    else:
        hs_codes = []

    if "Foreign Country" in df.columns:
        countries = df["Foreign Country"].dropna().unique().tolist()
    else:
        countries = []

    if "Importer Name" in df.columns:
        importers = df["Importer Name"].dropna().unique().tolist()
    else:
        importers = []

    col1, col2, col3 = st.columns(3)

    with col1:
        selected_hs = st.selectbox("Filter by HS Code", ["All"] + hs_codes if hs_codes else ["Not Available"])

    with col2:
        selected_country = st.selectbox("Filter by Country", ["All"] + countries if countries else ["Not Available"])

    with col3:
        selected_importer = st.selectbox("Filter by Importer", ["All"] + importers if importers else ["Not Available"])

    filtered_df = df.copy()
    if "HS Code" in df.columns and selected_hs != "All":
        filtered_df = filtered_df[filtered_df["HS Code"] == selected_hs]

    if "Foreign Country" in df.columns and selected_country != "All":
        filtered_df = filtered_df[filtered_df["Foreign Country"] == selected_country]

    if "Importer Name" in df.columns and selected_importer != "All":
        filtered_df = filtered_df[filtered_df["Importer Name"] == selected_importer]

    return filtered_df
