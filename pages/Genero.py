import streamlit as st;

from scripts.data_loader import load_data
from components.chart import display


# Load data
df = load_data()

#Page config
st.set_page_config(page_title="Genero", layout="wide")
st.markdown("# 🧑‍💼👩‍💼 Classificação por Gênero")


#Layout
## Chart column is wider
row1_col1, row1_col2 = st.columns([3,1])

f1_df = df.groupby('Gender')["Price"].agg('mean').reset_index()
with row1_col1:
    #Bar
    display(
        kind='bar',
        df=f1_df,
        group_col='Gender',
        value_col='Price',  # Make sure this matches an actual column in your DataFrame
        title='Preço Médios de Veiculos Adquiridos por Gênero'
    )

with row1_col2:
    st.markdown("**Descrição**")
    st.write("O gráfico apresenta a média de preços dos veículos adquiridos, segmentada por gênero dos compradores. Essa visualização permite identificar possíveis diferenças no comportamento de compra entre os diferentes grupos.")
    
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
        title='Contagem de Vendas por Gênero e Fabricante'
    )

with row2_col2:
    st.markdown("**Descrição**")
    st.write("O gráfico apresenta a quantidade de modelos de veículos vendidos, segmentada por gênero dos compradores e por fabricante (Company). Cada barra representa o número de transações associadas a homens e mulheres para cada marca de veículo registrada no conjunto de dados.")


st.markdown("---") 
# === Row3 ====
row3_col1, row3_col2 = st.columns([3,1])


with row3_col1:
    top_10 = df[df['Model'].isin(df['Model'].value_counts().head(10).index)]
    display(
        kind= 'bar_count',
        df = top_10,
        group_col='Model',
        value_col= None,
        title='Contagem dos 10 Modelos de Carros Mais Populares (Geral)'
    )

with row3_col2:
    st.markdown("**Descrição**")
    st.write(f"O gráfico exibe a quantidade de vendas dos 10 modelos de veículos mais populares, com base no número de ocorrências registradas no relatório de vendas. Cada barra representa um modelo específico e o total de vezes em que ele foi vendido. Essa visualização permite identificar quais modelos têm maior aceitação no mercado, sendo os preferidos pelos consumidores.Essa informação é extremamente útil para análises de demanda, controle de estoque, decisões de reposição e definição de estratégias comerciais.")






