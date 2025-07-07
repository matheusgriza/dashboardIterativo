import streamlit as st;
from scripts.data_loader import load_data;
from components.chart import display;


#Page config
st.set_page_config(page_title = "Vendas de Veículos", layout = "wide")

# Load data
df = load_data()

#Title
st.title("🚗 Dashboard de Vendas de Veículos")

# 📘 Curta documentação
st.markdown("""
### ℹ️ Sobre este dashboard

**Objetivo:**  
Este dashboard tem como objetivo fornecer uma visão clara sobre as vendas de carros, com base em informações filtráveis por gênero, preço, modelo e categoria.

**Como navegar entre as seções:**  
Use a barra lateral para alternar entre as diferentes páginas e análises disponíveis no sistema.

**Como os filtros influenciam os dados:**  
Todas as paginas estão estruturadas da mesma maneira. Utilize os filtros localizados acima do gráfico que deseja manipular para tanto.

**Abaixo encontra-se uma visualização do dataset completo, com um filtro opcional por gênero.**
""")


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




