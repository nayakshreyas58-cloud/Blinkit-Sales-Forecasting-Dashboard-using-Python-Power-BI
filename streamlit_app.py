import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Blinkit Analytics Dashboard",
    page_icon="🛒",
    layout="wide"
)

# Load Data
df = pd.read_excel("BlinkIT Grocery Data.xlsx")

# Sidebar Filters
st.sidebar.title("🛒 Blinkit Filters")

location_filter = st.sidebar.multiselect(
    "Outlet Location Type",
    options=df["Outlet Location Type"].unique(),
    default=df["Outlet Location Type"].unique()
)

size_filter = st.sidebar.multiselect(
    "Outlet Size",
    options=df["Outlet Size"].dropna().unique(),
    default=df["Outlet Size"].dropna().unique()
)

item_filter = st.sidebar.multiselect(
    "Item Type",
    options=df["Item Type"].unique(),
    default=df["Item Type"].unique()
)

df_filtered = df[
    (df["Outlet Location Type"].isin(location_filter)) &
    (df["Outlet Size"].isin(size_filter)) &
    (df["Item Type"].isin(item_filter))
]

# KPI Metrics
total_sales = df_filtered["Sales"].sum()
avg_sales = df_filtered["Sales"].mean()
num_items = len(df_filtered)
avg_rating = df_filtered["Rating"].mean()

st.title("🛒 Blinkit Analytics Dashboard")

col1, col2, col3, col4 = st.columns(4)

col1.metric("💰 Total Sales", f"${total_sales:,.0f}")
col2.metric("📈 Avg Sales", f"${avg_sales:.0f}")
col3.metric("📦 No Of Items", f"{num_items:,}")
col4.metric("⭐ Avg Rating", f"{avg_rating:.1f}")

st.markdown("---")

# Sales Trend
sales_trend = (
    df_filtered.groupby("Outlet Establishment Year")["Sales"]
    .sum()
    .reset_index()
)

fig_trend = px.line(
    sales_trend,
    x="Outlet Establishment Year",
    y="Sales",
    markers=True,
    title="Outlet Establishment Trend"
)

st.plotly_chart(fig_trend, use_container_width=True)

col5, col6 = st.columns(2)

# Item Type Sales
item_sales = (
    df_filtered.groupby("Item Type")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig_item = px.bar(
    item_sales,
    x="Sales",
    y="Item Type",
    orientation="h",
    title="Top Item Types By Sales"
)

col5.plotly_chart(fig_item, use_container_width=True)

# Outlet Size
size_sales = (
    df_filtered.groupby("Outlet Size")["Sales"]
    .sum()
    .reset_index()
)

fig_size = px.pie(
    size_sales,
    names="Outlet Size",
    values="Sales",
    hole=0.5,
    title="Sales By Outlet Size"
)

col6.plotly_chart(fig_size, use_container_width=True)

col7, col8 = st.columns(2)

# Fat Content
fat_sales = (
    df_filtered.groupby("Item Fat Content")["Sales"]
    .sum()
    .reset_index()
)

fig_fat = px.pie(
    fat_sales,
    names="Item Fat Content",
    values="Sales",
    hole=0.5,
    title="Sales By Fat Content"
)

col7.plotly_chart(fig_fat, use_container_width=True)

# Outlet Location
loc_sales = (
    df_filtered.groupby("Outlet Location Type")["Sales"]
    .sum()
    .reset_index()
)

fig_loc = px.bar(
    loc_sales,
    x="Outlet Location Type",
    y="Sales",
    title="Sales By Outlet Location"
)

col8.plotly_chart(fig_loc, use_container_width=True)

st.markdown("---")

st.subheader("📋 Dataset Preview")
st.dataframe(df_filtered, use_container_width=True)
