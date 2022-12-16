#Import Necessary Libraries
import streamlit as st
import docx2txt

st.title("DOCX & Text Documents")

# Defining File Uploader Function in a variable
text_file = st.file_uploader("Upload Document", type=["docx","txt"])

# Button to check document details
details = st.button("Check Details")

# Condition to get document details
if details:

    if text_file is not None:

        # Getting Document details like name, type and size  
        doc_details = {"file_name":text_file.name, "file_type":text_file.type,
                        "file_size":text_file.size}
        st.write(doc_details)
        
        # Check for text/plain document type
        if text_file.type == "text/plain":
            # Read document as string with utf-8 format
            raw_text = str(text_file.read(),"utf-8")
            st.write(raw_text)
            
        else:
            # Read docx document type
            docx_text = docx2txt.process(text_file) 
            st.write(docx_text)            