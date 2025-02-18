import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from pandas.tseries.offsets import BDay
from statsmodels.tsa.arima.model import ARIMAResults

months_pt = {
    'January': 'janeiro', 'February': 'fevereiro', 'March': 'março',
    'April': 'abril', 'May': 'maio', 'June': 'junho',
    'July': 'julho', 'August': 'agosto', 'September': 'setembro',
    'October': 'outubro', 'November': 'novembro', 'December': 'dezembro'
}

today = datetime.today()
month_pt = months_pt[today.strftime('%B')]
today_str = today.strftime(f'%d de {month_pt} de %Y')
st.write(f"Hoje é: **{today_str}**")

@st.cache_resource
def load_model():
    return ARIMAResults.load('PriceForecasting/arima_model.pkl')

model = load_model()

steps = st.number_input(
    'Quantos dias úteis você deseja prever?',
    min_value=1,
    max_value=30,
    value=7,
    step=1
)

if st.button('Atualizar Previsão'):
    forecast = model.forecast(steps=steps)
    future_dates = pd.date_range(datetime.today() + BDay(1), periods=steps, freq=BDay())

    forecast_df = pd.DataFrame({
        'Data': future_dates.strftime('%d/%m/%Y'),
        'Preço Previsto (USD)': forecast
    })

    st.success('Previsão gerada com sucesso!')
    st.dataframe(forecast_df, use_container_width=True, hide_index=True)

    maior_valor = forecast_df['Preço Previsto (USD)'].max()
    menor_valor = forecast_df['Preço Previsto (USD)'].min()
    data_maior_valor = forecast_df.loc[forecast_df['Preço Previsto (USD)'] == maior_valor, 'Data'].values[0]
    data_menor_valor = forecast_df.loc[forecast_df['Preço Previsto (USD)'] == menor_valor, 'Data'].values[0]

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Maior valor previsto (USD)", f"{maior_valor:.2f}")
        st.markdown(f"<div style='font-size: 14px; color: #6c757d;'>Em {data_maior_valor}</div>", unsafe_allow_html=True)

    with col2:
        st.metric("Menor valor previsto (USD)", f"{menor_valor:.2f}")
        st.markdown(f"<div style='font-size: 14px; color: #6c757d;'>Em {data_menor_valor}</div>", unsafe_allow_html=True)

    csv = forecast_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Baixar Previsão em CSV",
        data=csv,
        file_name=f'previsao_petroleo_{datetime.today().strftime("%d%m%Y")}.csv',
        mime='text/csv',
    )

st.info("As previsões consideram apenas dias úteis (segunda a sexta). Fins de semana e feriados não são incluídos.")