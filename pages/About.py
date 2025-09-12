import streamlit as st

# Configuração da página (wide mode, título, ícone)
st.set_page_config(
    page_title="How to Use",
    page_icon="📚",
    layout="wide"
)

st.title("⚙️ Learn How To Use This Tool")

with st.expander("⚙️ Expected cURL Format", expanded=False):
    st.write('Code example:')
    st.code(
        """
        curl --location 'URL HERE'
        --header 'Content-Type: application/json'
        --header 'Authorization: Bearer {{Token}}'
        --data-raw '{
        "email": "",
        "password": ""
        }'
        """)
    
with st.expander("⚠️ Invalid cURL Formats", expanded=False):
    st.write('Some softwares exports cURLs in different ways, like the example below')
    st.code(
        """
        curl --l 'URL HERE'
        --h 'Content-Type: application/json'
        --h 'Authorization: Bearer {{Token}}'
        --X '{
        "email": "",
        "password": ""
        }'
        """)
    
    st.write('To run this applicaton you must use the most common cURL patterns:')
    st.code(
        """
        curl --location 'URL HERE'
        --header
        --data-urlencode
        --data
        --data-raw
        --form
        """)

with st.expander("📎 Step by Step", expanded=False):
    st.write("First things first!")
    st.code("""Ex: curl --location 'https://url'
    --header 'Content-Type: application/json'
    --header 'Authorization: Bearer'
    --data-raw '{
    "name": "Name",
    }'""")
    st.write("1- Go to 'Robot Curl Converter' Page and paste your cURL code into the first field so the application could read the data.")
    st.write("2- Select the options that match your cURL structure")
    st.write("3- Click on 'Convert' button.")
    st.write("4- Voilà, Your code will be displayed at the bottom of the page.")

with st.expander("🔵 Contact", expanded=False):
    st.markdown("""
    <div style='text-align: center;'>
        <h3 style='margin-bottom: 1rem;'>👨‍💻 Juan Santos</h3>
        <p style='color: #666; margin-bottom: 1.5rem;'>
        Tech Lead QA Automation | Robot Framework Specialist
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Badges clicáveis
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style='text-align: center;'>
            <a href='https://github.com/tjuant1' target='_blank'>
                <img src='https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white' width='120'>
            </a>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='text-align: center;'>
            <a href='https://www.linkedin.com/in/juan-psantos/' target='_blank'>
                <img src='https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white' width='120'>
            </a>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style='text-align: center;'>
            <a href='mailto:juanpatrickpds@gmail.com'>
                <img src='https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white' width='120'>
            </a>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    st.markdown("""
    💼 **7 years of experience**\n
    🛠️ **Robot Framework, Playwright, Frontend, API REST, Desktop Automation, Mobile Automation, SAP Automation, Python**\n
    """)