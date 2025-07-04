import plotly.express as px
import streamlit as st

def generate_charts(df):
    if df.empty:
        st.warning("No data available for visualization.")
        return

    top_products = df.groupby('Product Description')['CIF Value (USD)'].sum().nlargest(10).reset_index()
    fig1 = px.bar(top_products, x='Product Description', y='CIF Value (USD)',
                  title='Top 10 Products by CIF Value', labels={'CIF Value (USD)': 'CIF Value'})
    st.plotly_chart(fig1, use_container_width=True)

    country_share = df.groupby('Foreign Country')['CIF Value (USD)'].sum().reset_index()
    fig2 = px.pie(country_share, names='Foreign Country', values='CIF Value (USD)', title='Import Share by Country')
    st.plotly_chart(fig2, use_container_width=True)
