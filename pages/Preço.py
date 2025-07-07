import streamlit as st;

from scripts.data_loader import load_data
from components.chart import display


# Load data
df = load_data()

#Page config
st.set_page_config(page_title="Preço", layout="wide")
st.markdown("# :moneybag: Preço")

col1, col2 = st.columns([3,1])

with col1:
    display("histogram", df, "Price", title = "Distribuição de Preço x Frequência")

with col2:
    st.markdown("### Descrição:")
    st.write("O gráfico acima apresenta a distribuição de frequência dos preços dos veículos vendidos, com base nos dados coletados no relatório de vendas. Através do histograma, é possível observar como os preços estão distribuídos ao longo de diferentes faixas, permitindo identificar as faixas de preço mais comuns entre os veículos vendidos.")
