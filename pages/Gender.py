import streamlit as st;

from scripts.data_loader import load_data
from components.chart import display


# Load data
df = load_data()

#Page config
st.set_page_config(page_title="Gender", layout="wide")
st.markdown("# 🧑‍💼👩‍💼 Data by Gender")


#Layout
## Chart column is wider
row1_col1, row1_col2 = st.columns([3,2])

f1_df = df.groupby('Gender')["Price"].agg('mean').reset_index()
with row1_col1:
    #Bar
    display(
        kind='bar',
        df=f1_df,
        group_col='Gender',
        value_col='Price',  # Make sure this matches an actual column in your DataFrame
        title='Average Age by Gender'
    )

with row1_col2:
    st.markdown("Chart description")
    st.write("This chart displays how much money each gender spends on cars")
    
st.markdown("---")

# === Row2 ====
row2_col1, row2_col2 = st.columns([3,1])


with row2_col1:
    #Count Bar
    display(
        kind= 'bar_count',
        df = df,
        group_col='Company',
        value_col= 'Gender',
        title='Counting Card Models per Gender'
    )

with row2_col2:
    st.markdown("Chart description")
    st.write("This chart displays which brand are prefered by gender")






