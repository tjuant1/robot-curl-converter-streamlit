import streamlit as st

# Configuração da página (wide mode, título, ícone)
st.set_page_config(
    page_title="cURL to Robot Framework Converter",
    page_icon="🤖",
    layout="wide"
)

st.title("🔗 cURL → Robot Framework Converter")

curl_input = st.text_area(
    "cURL Command:",
    height=240,
    placeholder="""Ex: curl --location 'https://url'
    --header 'Content-Type: application/json'
    --header 'Authorization: Bearer'
    --data-raw '{
    "name": "Name",
    }'
    """
    , key="curl_input")

output = st.info('This is a purely informational message', icon="ℹ️", key='output')