import streamlit as st

with st.container():
    st.subheader("Análise dos Resultados e Eficácia do Modelo na Previsão do Preço do Petróleo", divider="blue")
    st.markdown(
        """
        Dos resultados obtidos, observamos uma acurácia aproximada de **92.64%**, considerando a relação com o erro percentual médio (MAPE). Esse valor indica que o modelo apresentou um desempenho elevado em relação às previsões realizadas. Além disso, temos valores de MAPE, MAE e RMSE relativamente baixos, com destaque para o MAPE em torno de **7.36%**, o que indica que, em média, o erro percentual das previsões é baixo. Essas métricas confirmam a eficácia do modelo na previsão do preço do petróleo.
        """
    )

    st.subheader("Impacto", divider="blue")
    st.markdown(
        """
        Os resultados obtidos com o modelo **ARIMA (1, 1, 1)** têm um impacto significativo no contexto prático da tomada de decisões no mercado de petróleo. Uma previsão precisa do preço do petróleo é importante para uma variedade de setores, incluindo finanças, energia e comércio internacional. Com base nos resultados deste estudo, os tomadores de decisão podem criar planos de ação mais eficazes para mitigar riscos, otimizar investimentos e planejar estratégias de negócios.
        """
    )