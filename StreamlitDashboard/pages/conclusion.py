import streamlit as st

with st.container():
    st.subheader("Análise dos Resultados e Eficácia do Modelo na Previsão do Preço do Petróleo", divider="blue")
    st.markdown(
        """
        Dos resultados obtidos, observamos um R² de XX%, o que indica que o modelo está acertando aproximadamente XX% das previsões realizadas. Esse valor é considerado alto, pois está próximo de 100%, sugerindo que o modelo possui uma capacidade significativa de explicar a variabilidade nos dados e de fazer previsões precisas do preço do petróleo. Além disso, temos valores de MSE, MAE e RMSE próximos de zero, o que é bom. Essas métricas indicam que as previsões do modelo têm uma dispersão muito baixa em relação aos valores reais, o que confirma a sua eficácia na previsão do preço do petróleo.
        """
    )

    st.subheader("Impacto", divider="blue")
    st.markdown(
        """
        Os resultados obtidos com o modelo XXXXX têm um impacto significativo no contexto prático da tomada de decisões no mercado de petróleo. Uma previsão precisa do preço do petróleo é importante para uma variedade de setores, incluindo finanças, energia e comércio internacional. Com base nos resultados deste estudo, os tomadores de decisão podem criar planos de ação mais eficazes para mitigar riscos, otimizar investimentos e planejar estratégias de negócios.
        """
    )

