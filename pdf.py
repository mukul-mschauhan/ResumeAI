from pypdf import PdfReader
from typing_extensions import Concatenate
import streamlit as st

def read_pdf(pdf_doc):
    pdf = PdfReader(pdf_doc)
    raw_text = " "
    for i, page in enumerate(pdf.pages):
        content = page.extract_text()
        if content:
            raw_text+=content
    return (raw_text)

    