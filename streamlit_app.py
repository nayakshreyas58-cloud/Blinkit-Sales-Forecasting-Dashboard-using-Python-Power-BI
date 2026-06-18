import streamlit as st
import pandas as pd

st.title("Blinkit Analytics Dashboard")

df = pd.read_excel("BlinkIT Grocery Data.xlsx")

st.write("Dataset Preview")
st.dataframe(df.head())
