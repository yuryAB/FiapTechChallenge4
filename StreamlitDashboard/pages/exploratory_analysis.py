import streamlit as st
import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings( 'ignore' )

with st.container():
    st.subheader("Fonte dos Dados", divider="blue")
    st.markdown(
        """
            Os dados históricos do preço do petróleo foram extraídos do site do Instituto de Pesquisa Econômica Aplicada (Ipea). O Ipea disponibiliza uma série temporal detalhada com valores diários do preço do petróleo. Na data da exportação, foram obtidos os preços que abrangem o período de 02 de janeiro de 2004 até 31 de dezembro de 2024.

            Esses dados foram salvos em um arquivo de extensão csv, preparando-os para uma análise subsequente em Python. Esta preparação permite utilizar ferramentas avançadas de análise e visualização para explorar a variação dos preços ao longo do tempo.    
        """
    )

    st.subheader("Dashboard", divider="blue")
    st.markdown(
        """
            Para visualizar a variação do preço do petróleo ao longo do tempo, criamos o gráfico abaixo.
            Utilizar a barra deslizante abaixo para filtrar um período de tempo.
        """
    )

df = pd.read_csv("preco_petroleo.csv", sep=";", decimal=".")

# Converter a coluna "Data" para o formato de data
df["Data"] = pd.to_datetime(df["Data"], format="mixed")
df.set_index("Data", inplace=True)

data_inicial = df.index.min().to_pydatetime()
data_final = df.index.max().to_pydatetime()
intervalo_data = st.slider("Selecione o período para exibir no gráfico:", min_value=data_inicial, max_value=data_final,
                            value=(data_inicial, data_final))
df_filtered = df.loc[intervalo_data[0]:intervalo_data[1]]
st.line_chart(data=df_filtered, y="Preco", y_label = "Preço Petróleo (US$)", use_container_width=True)


