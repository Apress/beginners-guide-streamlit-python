import streamlit as st
import io
from PIL import Image


uploaded_files = st.file_uploader("Multiple Image Uploader", type=['jpg','jpeg','png'], 
                    help="Upload Images in jpg, jpeg, png format", accept_multiple_files=True,)
details = st.button("Check Details")

for uploaded_file in uploaded_files:
    if details:
        if uploaded_file is not None:

            bytes_data = uploaded_file.read()
            image = Image.open(io.BytesIO(bytes_data))
            st.write("file_name:", uploaded_file.name)
            st.image(image, width=100)
            
        else:
            st.write("No Image File is Uploaded")
            break
        
    