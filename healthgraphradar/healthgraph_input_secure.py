import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import os

def login():
    st.sidebar.subheader("🔐 Login de Acesso")
    usuario = st.sidebar.text_input("Usuário")
    senha = st.sidebar.text_input("Senha", type="password")
    engine = create_engine(os.getenv("DB_URL"))
    query = "SELECT * FROM usuarios WHERE usuario = %s AND senha = %s AND ativo = TRUE"
    df = pd.read_sql(query, con=engine, params=(usuario, senha))

    if not df.empty:
        st.session_state["usuario"] = df.iloc[0]["usuario"]
        return True
    else:
        if usuario and senha:
            st.sidebar.error("Usuário ou senha inválidos.")
        return False