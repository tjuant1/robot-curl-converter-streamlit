import streamlit as st

# Configuração da página (wide mode, título, ícone)
st.set_page_config(
    page_title="Home",
    layout="wide"
)

st.title("🔗 Conversor cURL → Robot Framework Test")

st.markdown("""
Bem-vindo! Use as páginas no menu lateral para:
- **🔄 Robot Curl Converter**: Transforme comandos cURL em scripts Robot prontos
- **📚 About**: Aprenda a usar a ferramenta
""")
