import streamlit as st;
from scripts.data_loader import load_data
from components.chart import display
import pandas as pd
#Page config
st.set_page_config(page_title="Modelo", layout="wide")
st.markdown("# 🚘 Vendas por Modelo e Categoria")

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
        title='Carros mais populares entre gêneros',
        yAxisTitle = 'Count'
    )

with text_col1:
    st.markdown("### **Descrição**")
    st.write("Este gráfico apresenta a contagem das vendas dos modelos de veículos mais populares, segmentadas por gênero dos compradores.\n\n O usuário pode escolher quantos dos principais modelos deseja visualizar (top 5, 10 ou 15) e também pode filtrar os dados por marca específica ou analisar todas as marcas juntas.")


st.markdown("---")

col3, col4, col5 = st.columns(3)

with col3:
    body_style_opt = ["All"] + sorted(df['Body Style'].unique())

    body_style = st.selectbox(
    "Body Style",
    options = body_style_opt,
    )

with col4:
    min_price = df['Price'].min()
    max_price = df['Price'].max()
    
    price_slider = st.slider(
        "Select Max Price",
        min_value = int(1200),
        max_value = int(85000),
        value = (min_price + max_price) // 2,
        step = 1000,
        format = "$%d"
    )
with col5:
    auto = st.checkbox("Auto")
    manual = st.checkbox("Manual")
   

f2_df = df.copy()

f2_df = f2_df[f2_df["Price"] <= price_slider]

if body_style != "All":
    f2_df = f2_df[f2_df["Body Style"] == body_style]

if(auto and not(manual)):
    f2_df = f2_df[f2_df["Transmission"] == "Auto"]
elif(manual and not(auto)):
    f2_df = f2_df[f2_df["Transmission"] == "Manual"]
    
f2_df = f2_df.sort_values(by="Price", ascending=False).head(30)

display(
    kind='bar',
    df=f2_df,
    group_col='Model',
    value_col='Price',
    yAxisTitle='Count'
)




