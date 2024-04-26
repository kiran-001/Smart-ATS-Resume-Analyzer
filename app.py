# Import all neccessary libraries
from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai
from PIL import Image 
import PyPDF2 as pdf

# Load the environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Configure the Generative AI API with the API key
genai.configure(api_key=api_key)

def get_gemini_response(input_text):
    """Use the Gemini Pro model to generate a response based on the input text."""
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input_text)
    return response.text

def extract_text_from_pdf(uploaded_file):
    """Extract text from each page of the uploaded PDF file."""
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""  # Append empty string if extract_text returns None
    return text

# Streamlit App
st.title("Smart Application Tracking System")
st.subheader("Optimize Your Resume for ATS")

# User input for job description and resume upload
jd = st.text_area("Paste the Job Description", height=150)
uploaded_file = st.file_uploader("Upload Your Resume", type=["pdf"], help="Please upload in PDF format.")

if st.button("Analyze Resume"):
    if uploaded_file and jd:
        resume_text = extract_text_from_pdf(uploaded_file)
        input_prompt = f"""
        {{
            "resume": "{resume_text}",
            "description": "{jd}",
            "request": "Evaluate the resume based on the job description. Assign a percentage match and suggest improvements."
        }}
        """
        response = get_gemini_response(input_prompt)
        
        # Directly display the response as it's not in JSON format
        st.markdown("### Evaluation Report")
        st.markdown(response)
    else:
        st.warning("Please ensure both a resume is uploaded and a job description is entered.")
