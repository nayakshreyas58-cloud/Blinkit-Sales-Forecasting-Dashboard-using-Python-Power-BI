import streamlit as st
import pandas as pd

st.set_page_config(page_title="Blinkit Dashboard", layout="wide")

df = pd.read_excel("BlinkIT Grocery Data.xlsx")

st.title("🛒 Blinkit Analytics Dashboard")

st.write("Columns in Dataset:")
st.write(df.columns.tolist())
