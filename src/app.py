import streamlit as st
import os
import sys

sys.path.append(os.path.dirname(__file__))
from queries import get_all_characters, get_characters_by_attribute

st.set_page_config(page_title="7DS Personagens", layout="wide")

st.title("📖 7DS - Personagens")

tab1, tab2 = st.tabs(["Todos os Personagens", "Filtro por Atributo"])

with st.sidebar:
    st.title("🔍 Buscar personagens")
    attribute = st.selectbox("Filtrar por atributo", ["", "STR", "SPD", "HP", "DARK", "LIGHT"])
    search_name = st.text_input("Buscar por nome")

if attribute or search_name:
    characters_df = get_characters_by_attribute(attribute) if attribute else get_all_characters()
    if search_name:
        characters_df = characters_df[characters_df['charactername'].str.contains(search_name, case=False)]
else:
    characters_df = get_all_characters()

st.dataframe(characters_df, use_container_width=True)
