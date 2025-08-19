import streamlit as st
from structure import GetContent

"""Variables"""
main_text_options = '--Select One Option--'

# Configuração da página (wide mode, título, ícone)
st.set_page_config(
    page_title="cURL to Robot Framework Converter",
    page_icon="🤖",
    layout="wide"
)

st.title("🔗 cURL → Robot Framework Converter")

"""User Curl Input"""
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

"""Select the body prefix"""
body_options = [main_text_options, '--data', '--data-raw', '--form', '--data-urlencode']
body_selected = st.selectbox(
    label="Select the body prefix",
    label_visibility="collapsed",
    index=0,
    options=body_options
)

"""Appears when --form is selected, define if the form has file"""
file_options = [main_text_options, 'Yes', 'No']
if body_selected == '--form':
    file_option = st.selectbox(
    label="Your Request Has A File?",
    index=0,
    options=file_options
    )

"""Select the headers prefix"""
headers_options = [main_text_options, '--header']
header_selected = st.selectbox(
    label="Select the body prefix",
    label_visibility='collapsed',
    index=0,
    options=headers_options
)

if curl_input:
    structure = GetContent()
    headers = structure.get_headers(curl_input, header_selected)
    url = structure.get_url(curl_input)
    print(url)

"""Automation code retuned to the user"""
output = "a"
st.info(f"""
        This is a purely informational message.\n
        {output}
        """, icon="ℹ️")