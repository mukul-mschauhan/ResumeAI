from pdf import read_pdf
import google.generativeai as genai
import streamlit as st

import os
genai.configure(api_key=os.getenv("GOOGLE-API-KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

# Read the pdf
def profile(pdf_doc, job_desc):
    if pdf_doc is not None:
        pdf = read_pdf(pdf_doc)
        st.sidebar.markdown("✅ Resume has been Uploaded")
    else:
        st.warning("Upload the Resume")
        
    ats_score = model.generate_content(f"Compare the {job_desc} with the resume {pdf} and suggest the ATS Score of the resume (in percentage)")
    probability = model.generate_content(f"Compare the {job_desc} with the resume {pdf} and suggest the probability (in percentage) of getting selected")
    keywords = model.generate_content(f"Compare the {job_desc} with the resume {pdf} and do a Keyword Analysis and mention the Missing Keywords in Bullet Points")
    improvements = model.generate_content(f"Compare the {job_desc} with the resume {pdf} and suggest Improvements in the resume that are aligned with Job Desc")
    projects = model.generate_content(f"Compare the {job_desc} with the resume {pdf} and suggest Projects/ML Competitions that are aligned with JD. ")
    
    # Display the Results
    return(st.write(ats_score.text),
           st.write(probability.text),
           st.write(keywords.text),
           st.write(improvements.text),
           st.write(projects.text))
