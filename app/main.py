import streamlit as st
import os
import requests
from langchain_community.document_loaders import WebBaseLoader, PyPDFLoader
from chains import Chain
from portfolio import Portfolio
from utils import clean_text

def get_github_data(username):
    if not username: return ""
    try:
        response = requests.get(f"https://api.github.com/users/{username}/repos")
        if response.status_code == 200:
            repos = response.json()
            langs = set([r['language'] for r in repos if r['language']])
            return f"Tech stack from GitHub: {', '.join(list(langs)[:5])}"
    except:
        return ""
    return ""

st.markdown("""
    <style>
    /* Hide the standard Streamlit footer and header */
    .stAppDeployButton {display:none;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Fix the main container to prevent scrolling */
    .main .block-container {
        max-height: 100vh;
        overflow: hidden;
        padding-top: 2rem;
        padding-bottom: 0rem;
    }

    /* Style for your "Created By Vision" footer */
    .custom-footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: transparent;
        color: #888;
        text-align: center;
        padding: 5px;
        font-size: 12px;
        z-index: 999;
    }
    </style>
    <div class="custom-footer">Created By Vision</div>
    """, unsafe_allow_html=True)

def create_streamlit_app(llm, portfolio, clean_text):
    st.title("🚀JobReach.Ai | A Universal AI Job Outreach Assistant")
    
    # User-specific inputs
    col1, col2 = st.columns(2)
    with col1:
        user_name = st.text_input("Enter Your Full Name:", placeholder="e.g. Nagendra Kumar")
    with col2:
        github_user = st.text_input("Enter GitHub Username:", placeholder="e.g. nagendra31")

    uploaded_file = st.file_uploader("Upload Your Resume (PDF)", type="pdf")

    portfolio_file = st.file_uploader("Upload your Portfolio CSV", type="csv")
    if portfolio_file:
        portfolio = Portfolio(file_path=portfolio_file)

    resume_text = ""
    
    if uploaded_file:
        with open("temp_res.pdf", "wb") as f:
            f.write(uploaded_file.getbuffer())
        loader = PyPDFLoader("temp_res.pdf")
        resume_text = "\n".join([p.page_content for p in loader.load()])
        os.remove("temp_res.pdf")
        st.success("Resume context uploaded!")

    url_input = st.text_input("Job Posting URL:")
    submit_button = st.button("Generate Cold Email")

    if submit_button:
        if not user_name or not resume_text:
            st.warning("Please provide your name and upload a resume first.")
            return

        try:
            github_stats = get_github_data(github_user)
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            portfolio.load_portfolio()
            jobs = llm.extract_jobs(data)
            
            for job in jobs:
                links = portfolio.query_links(job.get('skills', []))
                email = llm.write_mail(job, links, resume_text, github_stats, user_name)
                st.code(email, language='markdown')
        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    st.set_page_config(layout="wide", page_title="Job Assistant")
    create_streamlit_app(Chain(), Portfolio(), clean_text)