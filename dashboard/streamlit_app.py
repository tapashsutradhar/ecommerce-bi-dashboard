import streamlit as st
import pandas as pd


st.title("E-commerce BI Dashboard")
df = pd.read_csv('../data/processed/ecommerce_cleaned.csv')
df['OrderDate'] = pd.to_datetime(df['OrderDate'])


st.metric("Total Revenue", df['TotalAmount'].sum())
st.metric("Total Orders", df['OrderID'].nunique())


monthly = df.groupby(df['OrderDate'].dt.to_period('M'))['TotalAmount'].sum().to_timestamp()
st.line_chart(monthly)


# Top Products
top_products = df.groupby('ProductName')['Quantity'].sum().sort_values(ascending=False).head(10)
st.bar_chart(top_products)