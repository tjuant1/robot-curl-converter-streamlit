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

"""Select the body prefix"""
body_options = ['--Select One Option--', '--data', '--data-raw', '--form', '--data-urlencode']
body_selected = st.selectbox(
    label="Select the body prefix",
    label_visibility="collapsed",
    index=0,
    options=body_options
)

file_options = ['--Select One Option--', 'Yes', 'No']
if body_selected == '--form':
    file_option = st.selectbox(
    label="Your Request Has A File?",
    index=0,
    options=file_options
    )

"""Select the body prefix:"""
headers_options = ['--Select One Option--', '--header']
body_selected = st.selectbox(
    label="Select the body prefix",
    label_visibility='collapsed',
    index=0,
    options=headers_options
)

output = "a"
st.info(f"""
        This is a purely informational message.\n
        {output}
        """, icon="ℹ️")

#print(curl_input)
st.session_state