import streamlit as st
import pdfplumber

st.title("PDF File")
pdf_file = st.file_uploader("Upload PDF", type=["pdf"])

details = st.button("Check Details")	
if details :

    if pdf_file is not None:

        pdf_details = {"file_name":pdf_file.name, "file_type":pdf_file.type,
                        "file_size":pdf_file.size}
        st.write(pdf_details)
        pdf = pdfplumber.open(pdf_file)
        pages = pdf.pages[0]
        st.write(pages.extract_text())
    else:
        st.write("No PDF File is Uploaded")

