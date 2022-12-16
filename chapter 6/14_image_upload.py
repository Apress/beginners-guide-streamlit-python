import streamlit as st
from PIL import Image
import io

st.title("Upload Image")
image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])

check_details = st.button("Check Details")
if check_details:
        
    if image_file is not None:

            # To See details
            image_details = {"file_name":image_file.name, "file_type":image_file.type,
                            "file_size":image_file.size}
            st.write(image_details)

            # To View Uploaded Image
            image_data = image_file.read()
            image = Image.open(io.BytesIO(image_data))
            st.image(image, width=250)

    else:
        st.write("No Image File is Uploaded")