import streamlit as st;
from scripts.data_loader import load_data;

#Page config
st.set_page_config(page_title = "Car Sale Dashboard", layout = "wide")

#Title
st.title("🚗 Car Sales Report Dashboard")


#Load data
df = load_data();

#Display data
st.subheader("Dataset Overview");
st.dataframe(df);