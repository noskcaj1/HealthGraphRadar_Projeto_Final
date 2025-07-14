import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
import os

def render_dashboard():
    st.subheader("📊 Painel de Análise de Dados Clínicos")

    engine = create_engine(os.getenv("DB_URL"))
    df = pd.read_sql("SELECT * FROM prontuarios", con=engine)

    st.dataframe(df)

    if not df.empty:
        col1, col2 = st.columns(2)
        with col1:
            fig = px.histogram(df, x="idade", title="Distribuição de Idades")
            st.plotly_chart(fig, use_container_width=True)
        with col2:
            fig2 = px.pie(df, names="sexo", title="Distribuição por Sexo")
            st.plotly_chart(fig2, use_container_width=True)