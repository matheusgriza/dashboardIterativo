import streamlit as st;

from scripts.data_loader import load_data
from components.chart import display


# Load data
df = load_data()

#Page config
st.set_page_config(page_title="By Gender", layout="wide")



#Chart
display(
    kind= 'bar',
    df = df,
    group_col='Gender',
    value_col='Price',
    title='Average Age by Gender'
)


display(
    kind= 'bar_count',
    df = df,
    group_col='Company',
    value_col= 'Gender',
    title='Counting Card Models per Gender'
)

