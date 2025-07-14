import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import os
from datetime import datetime

def form_input():
    st.subheader("📥 Cadastro de Prontuário Clínico")

    with st.form("formulario"):
        nome = st.text_input("Nome do Paciente")
        idade = st.number_input("Idade", min_value=0, max_value=130)
        sexo = st.selectbox("Sexo", ["Masculino", "Feminino", "Outro"])
        sintomas = st.text_area("Sintomas")
        diagnostico = st.text_area("Diagnóstico")
        profissional_id = st.text_input("ID do Profissional")

        submitted = st.form_submit_button("Salvar")

        if submitted:
            if nome and profissional_id:
                engine = create_engine(os.getenv("DB_URL"))
                with engine.begin() as conn:
                    conn.execute(
                        "INSERT INTO prontuarios (nome, idade, sexo, sintomas, diagnostico, profissional_id, data_insercao) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                        (nome, idade, sexo, sintomas, diagnostico, profissional_id, datetime.now())
                    )
                st.success("Dados salvos com sucesso!")
            else:
                st.error("Preencha todos os campos obrigatórios.")