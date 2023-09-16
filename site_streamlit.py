import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard finanças")

with st.container():
    st.subheader("Site com dashboard")
    st.title("Dashboard de contratos")
    st.write("Informações de contrato fechado com a hash")

@st.cache_data
def carregar_dados():
    tabela = pd.read_csv("resultados.csv")
    return tabela

with st.container():
    st.write("---")
    qtde_dias = st.selectbox("Selecione a quantidade de dias", ["7d", "15d", "21d", "30d"])
    num_dias = int(qtde_dias.replace("d", ""))
    dados = carregar_dados()
    dados = dados[-num_dias:]
    st.area_chart(dados, x = "Data", y = "Contratos" )