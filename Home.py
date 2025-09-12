import streamlit as st

# Configuração da página (wide mode, título, ícone)
st.set_page_config(
    page_title="Home",
    layout="wide"
)

st.title("🔗 cURL → Robot Framework Converter")

st.markdown("""
Welcome! Use side tabs to:
- **🔄 Robot Curl Converter**: Convert cURL commands into Robot Framework script ready to use
- **📚 About**: Learn how to use the tool
""")