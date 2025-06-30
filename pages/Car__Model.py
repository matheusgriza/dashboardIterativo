import streamlit as st;
from scripts.data_loader import load_data
from components.chart import display

#Page config
st.set_page_config(page_title="By Car Model & Brand", layout="wide")
st.markdown("# 🚘 Sales by Car Model")

# Load data
df = load_data()

# Layout
# Chart column is wider
col1, col2 = st.columns(2)

with col1:
    topPicked = st.selectbox(
    "Top",
    [5,10,15]
    )

with col2:
    brand = st.selectbox(
        "Brand",
        ['All'] + sorted(df['Company'].unique()),
    )



# Filters
f1_df = df.copy()
if(brand != "All"):
    f1_df = f1_df[f1_df["Company"] == brand]

top_models = f1_df['Model'].value_counts().nlargest(topPicked).index
f1_df = f1_df[f1_df["Model"].isin(top_models)]



chart_col1, text_col1 = st.columns([2,1])
with chart_col1:
    #Count Bar
    display(
        kind= 'bar_count',
        df = f1_df,
        group_col='Model',
        value_col= 'Gender',
        title='Most popular model between genders',
        yAxisTitle = 'Count'
    )

with text_col1:
    st.markdown("### Chart Description")
    st.write("This is the chart description")


st.markdown("---")

col3, col4 = st.columns(2)

with col3:
    body_style_opt = ["All"] + sorted(df['Body Style'].unique())

    body_style = st.selectbox(
    "Body Style",
    options = body_style_opt,
    )

with col4:
    min_price = df['Price'].min()
    max_price = df['Price'].max()
    price_options = list(range(min_price, max_price + 1))
    
    price_slider = st.select_slider(
    "Select Max Price",
    options= price_options,
    format_func = lambda x: f"${x:,.0f}" 
    )
   

#Filter
f2_df = df.copy()

f2_df = f2_df[f2_df["Price"] <= price_slider]

if(body_style != "All"):
    f2_df = f2_df[f2_df["Body Style"] == body_style]

f2_df = f2_df.sort_values(by="Price", ascending=False).head(10)


display(
    kind= 'bar',
    df = f2_df,
    group_col='Model',
    value_col= 'Price',
    title = 'Most expensive cars',
    yAxisTitle = 'Count'
)







