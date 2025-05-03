# Setup the Local Environment
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import google.generativeai as genai
from pdf import read_pdf
from analysis import profile

# Create the Streamlit Front End
st.header("📝 Resume Analysis :blue[Your Job Companion]✍️", divider="green")
st.subheader("✅ Tips for Using the Application")

notes = f'''
* **Upload the resume (PDF):** Please upload your resume for the Analysis. It is an application powered by Google Gemini
* **Paster the Job Desc:** Please copy paste the Job Description for the Analysis.
* **Unleash the Power of Gemini:** Watch as the AI model digs deeper into the Resume and Draw Insights'''
st.write(notes)

st.sidebar.subheader("⬆️ Upload the Resume 📤")
pdf_doc = st.sidebar.file_uploader("Upload your Resume", type = ["pdf"])

st.subheader("Enter the Job Description", divider=True)
job_desc = st.text_area(label = "Copy Paste the Job Description from Linkedin or any Job Portal",
                        max_chars=10000)

button = st.button(label="Get AI Powered Insights")
if button:
    st.markdown(profile(pdf_doc=pdf_doc, job_desc=job_desc))



