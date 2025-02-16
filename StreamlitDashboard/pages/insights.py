import streamlit as st

with st.container():
    st.subheader("", divider="blue")
    st.markdown(
        """
                A compreensão dos eventos que impactam o mercado de petróleo é essencial para prever flutuações nos preços. Analisando o dashboard, observamos algumas flutuações que podem ter sido reflexo dos eventos abaixo listados.\n
                :one: **COVID-19:**\n
                A eclosão da pandemia da Covid-19 levou o preço do petróleo ao menor valor em 2020 quando o medo generalizado de uma recessão global derrubou os preços de petróleo a ponto de o contrato futuro WTI (referência de preço no mercado americano) ser cotado a preços negativos, um evento sem precedentes na história.

                :two: **Guerra Rússia x Ucrânia:**\n
                O salto observado em março de 2022 reflete a eclosão da guerra entre Rússia e Ucrânia, dado o envolvimento direto no conflito de um dos maiores produtores da commodity do mundo e as esperadas sanções impostas à comercialização de petróleo russo, que reduziram a oferta e elevaram o preço de energia ao redor do mundo. 

                :three: **Crise econômica de 2008:**\n
                A disparada nos preços veio em duas ondas: imediatamente após o início da crise — nos meses antecedentes à quebra do Lehman Brothers — e em 2009, quando a recuperação econômica global começou. A falência do banco, que virou símbolo do período, ocorreu em setembro de 2008. De abril a junho, a alta no preço do barril foi de 46%. O recorde no valor do Brent é dessa época.

                :four: **Tensões geopolíticas:**\n
                Em janeiro de 2016 o preço do petróleo teve seu menor valor desde 2004. Na ocasião, o que assustou o mercado foi um intenso e inesperado aumento nos estoques de gasolina dos Estados Unidos. Além disso, tensões geopolíticas após o anúncio de um teste de bomba de hidrogênio pela Coreia do Norte contribuíram para o tombo dos preços no começo do ano.
                Ao mesmo tempo, a perspectiva de demanda menor da Europa e da Ásia devido ao menor crescimento da economia no mundo também contribuiu para a queda.
        """
    )

