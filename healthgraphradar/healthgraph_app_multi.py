import streamlit as st
from healthgraph_input_front import form_input
from healthgraph_dashboard import render_dashboard

def render_paginas():
    menu = ["📥 Cadastro", "📊 Análise"]
    escolha = st.sidebar.radio("Menu", menu)

    if escolha == "📥 Cadastro":
        form_input()
    elif escolha == "📊 Análise":
        render_dashboard()