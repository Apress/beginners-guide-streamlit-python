# Import following libraries
import streamlit as st
from PIL import Image
import os
import io

# Defining File Upload Method of Streamlit
st.title("Saving File to Directory")
image_file = st.file_uploader("Upload Images",
			type=["png","jpg","jpeg"])

# Defining path where file to be saved
file_save_path = "F:/Books/Apress Streamlit/Chapters/02 Codes/chapter 6 forms/save"    


save_file = st.button("Check Details & Save")
if save_file:
        
    if image_file is not None:

            # To See details
            image_details = {"file_name":image_file.name, "file_type":image_file.type,
                            "file_size":image_file.size}
            st.write(image_details)

            # To View Uploaded Image
            image_data = image_file.read()
            image = Image.open(io.BytesIO(image_data))
            st.image(image, width=250)

            with open(os.path.join(file_save_path,image_file.name),"wb") as f:
                f.write((image_file).getbuffer())
            
            st.success("Image Saved Successfully")


    else:
        st.write("No Image File is Uploaded")