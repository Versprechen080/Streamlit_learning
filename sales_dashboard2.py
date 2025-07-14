import streamlit as st
import pandas as pd

st.set_page_config(page_title="Sales Dashboard", layout="wide")
# title
st.title("📊 Sales Dashboard")

df = pd.read_csv("sales.csv")

# Display raw data
st.subheader("Raw data")
st.dataframe(df)

# Select salesperson
salespeople = df["Salesperson"].unique()
selected_person = st.selectbox("Select a Salesperson", salespeople)

# Filer data
filtered_df = df[df["Salesperson"] == selected_person]

# Display filtered data
st.subheader(f"Sales Data for {selected_person}")
st.dataframe(filtered_df)

# Show total revenue
total_revenue = filtered_df["Revenue"].sum()
st.metric("💰 Total Revenue", f"${total_revenue}")
