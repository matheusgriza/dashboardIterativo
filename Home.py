import streamlit as st;
from scripts.data_loader import load_data;
from components.chart import display;


#Page config
st.set_page_config(page_title = "Car Sale Dashboard", layout = "wide")

# Load data
df = load_data()

#Title
st.title("🚗 Car Sales Report Dashboard")

st.subheader("Dataset Overview")
gender_options = ["Any"] + sorted(df['Gender'].unique().tolist())
genderPicked = st.selectbox(
    "Pick a gender to see",
    gender_options
)

if(genderPicked == "Any"):
    filtered_data = df
else:
    filtered_data = df[df['Gender'] == genderPicked]

st.write("Selected Option")
st.dataframe(filtered_data)




