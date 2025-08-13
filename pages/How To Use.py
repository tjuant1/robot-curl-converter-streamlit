import streamlit as st

# Configuração da página (wide mode, título, ícone)
st.set_page_config(
    page_title="How to Use",
    page_icon="📚",
    layout="wide"
)

st.title("⚙️ Learn How To Use This Tool")

st.info(
    """
    Some information
    """)

st.markdown("### cURL example:")

st.code(
    """
    curl --location 'https://nest-erp.qacoders-academy.com.br//api/auth/login'
    --header 'Content-Type: application/json'
    --header 'Authorization: Bearer {{Token}}'
    --data-raw '{
    "email": "sysadmin@qacoders.com",
    "password": "1234@Test"
    }'
    """)