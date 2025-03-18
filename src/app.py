import streamlit as st
from queries import get_all_characters, get_characters_by_attribute
import os

st.set_page_config(page_title="7DS - Personagens", layout="wide")

# Diretórios
ICON_PATH = os.path.join(os.path.dirname(__file__), '..', 'assets', 'images', 'icon')
IMG_PATH = os.path.join(os.path.dirname(__file__), '..', 'assets', 'images', 'personagens')

attr_styles = {
    "STR": {"color": "#FF4B4B", "icon": "str.png"},
    "SPD": {"color": "#4B9EFF", "icon": "spd.png"},
    "HP": {"color": "#4BFF62", "icon": "hp.png"},
    "LIGHT": {"color": "#FFD700", "icon": "light.png"},
    "DARK": {"color": "#A020F0", "icon": "dark.png"},
}

# Sidebar com filtros
with st.sidebar:
    st.image("https://i.ytimg.com/vi/W6urjOlb7qg/maxresdefault.jpg", use_container_width=True)
    st.header("🎯 Filtros")
    attribute = st.selectbox("🔮 Filtrar por Atributo:", ["", "STR", "SPD", "HP", "LIGHT", "DARK"])
    search_name = st.text_input("🔍 Buscar por Nome:")

# Query de personagens
if attribute:
    df = get_characters_by_attribute(attribute)
else:
    df = get_all_characters()

if search_name:
    df = df[df['charactername'].str.contains(search_name, case=False)]

# Página principal
st.title("⚔️ Nanatsu no Taizai - Lista de Personagens")
st.markdown(f"### 📊 Total de personagens encontrados: **{len(df)}**")
st.markdown("---")

# Renderização dos cards
for idx, row in df.iterrows():
    attr = row['characteratribute']
    style = attr_styles.get(attr, {"color": "#999", "icon": ""})

    # Verificar imagem .png ou .jpg
    id_img = str(row['id'])
    png_path = os.path.join(IMG_PATH, f"{id_img}.png")
    jpg_path = os.path.join(IMG_PATH, f"{id_img}.jpg")
    jpeg_path = os.path.join(IMG_PATH, f"{id_img}.jpeg")
    webp_path = os.path.join(IMG_PATH, f"{id_img}.webp")

    if os.path.exists(png_path):
        char_img = png_path
    elif os.path.exists(jpg_path):
        char_img = jpg_path
    elif os.path.exists(jpeg_path):
        char_img = jpeg_path
    elif os.path.exists(webp_path):
        char_img = webp_path
    else:
        char_img = None

    # Card com Expander
    with st.container():
        with st.expander(f"{row['charactername']}"):
            st.markdown(f"<p style='font-size: 14px; color: #AAAAAA; margin-top: -10px;'>{row['charactertitle']}</p>", unsafe_allow_html=True)

            cols = st.columns([1, 4])
            with cols[0]:
                if char_img:
                    st.image(char_img, width=100)
                else:
                    st.warning("Imagem não encontrada!")

            with cols[1]:
                st.markdown(f"**✨Atributo:**")
                if style['icon']:
                    st.image(os.path.join(ICON_PATH, style['icon']), width=100)
                
