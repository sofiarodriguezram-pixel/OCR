import streamlit as st
import cv2
import numpy as np
import pytesseract
from PIL import Image

# --- Configuración de la página ---
st.set_page_config(
    page_title="Reconocimiento Óptico de Caracteres",
    page_icon="🔠",
    layout="centered"
)

# --- Estilos personalizados ---
page_style = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');

    html, body, [class*="st-"], [data-testid="stAppViewContainer"] * {
        font-family: 'Poppins', sans-serif !important;
    }

    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #e3f2fd, #fce4ec, #f3e5f5);
        color: #333;
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #e1f5fe, #f3e5f5);
        color: #333;
    }

    /* Título con sombra y degradado */
    h1, .stMarkdown h1 {
        text-align: center;
        font-weight: 700 !important;
        background: linear-gradient(90deg, #ff6ec7, #9b5de5, #4361ee);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.3em !important;
        padding: 0.2em 0;
        text-shadow: 2px 2px 10px rgba(100, 100, 255, 0.25);
    }

    .stRadio > div {
        background-color: #ffffffa8 !important;
        border-radius: 10px !important;
        padding: 10px !important;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

    .stButton > button {
        background: linear-gradient(90deg, #9b5de5, #4361ee);
        color: white !important;
        border-radius: 10px;
        border: none;
        font-weight: 600;
        transition: all 0.3s ease;
    }

    .stButton > button:hover {
        background: linear-gradient(90deg, #4361ee, #9b5de5);
        transform: scale(1.03);
    }

    .stCameraInput {
        border: 2px solid #9b5de5 !important;
        border-radius: 15px !important;
        box-shadow: 0 3px 6px rgba(0,0,0,0.1);
        padding: 10px;
    }

    .stMarkdown {
        color: #333;
    }
</style>
"""
st.markdown(page_style, unsafe_allow_html=True)

# --- Título ---
st.markdown("<h1>🔠 Reconocimiento Óptico de Caracteres (OCR)</h1>", unsafe_allow_html=True)

# --- Interfaz principal ---
img_file_buffer = st.camera_input("📸 Toma una Foto")

with st.sidebar:
    st.subheader("🎨 Opciones de Filtro")
    filtro = st.radio("Aplicar Filtro", ('Con Filtro', 'Sin Filtro'))

# --- Procesamiento de imagen ---
if img_file_buffer is not None:
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    
    if filtro == 'Con Filtro':
        cv2_img = cv2.bitwise_not(cv2_img)
    
    img_rgb = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
    text = pytesseract.image_to_string(img_rgb)

    st.markdown("### 🧾 Texto Detectado:")
    st.write(text)
