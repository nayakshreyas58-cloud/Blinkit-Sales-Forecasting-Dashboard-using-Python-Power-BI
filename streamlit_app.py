import streamlit as st
import pandas as pd

st.set_page_config(page_title="Blinkit Analytics Dashboard", layout="wide")

st.title("🛒 Blinkit Analytics Dashboard")

df = pd.read_excel("BlinkIT Grocery Data.xlsx")

st.subheader("Dataset Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Total Records", len(df))
col2.metric("Columns", len(df.columns))
col3.metric("Missing Values", df.isnull().sum().sum())

st.subheader("Data Preview")
st.dataframe(df)

st.subheader("Column Names")
st.write(list(df.columns))
