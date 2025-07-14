import streamlit as st
from healthgraph_app_multi import render_paginas
from healthgraph_input_secure import login

st.set_page_config(page_title="HealthGraph Radar", layout="wide", initial_sidebar_state="expanded")

if login():
    render_paginas()