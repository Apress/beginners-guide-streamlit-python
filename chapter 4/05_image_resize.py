import streamlit as st
from PIL import Image

original_image = Image.open("files/animal9.jpg")

# Display Original Image
st.title("Original Image")
st.image(original_image)

# Resizing Image to 600*400 
resized_image = original_image.resize((600, 400))

#Displaying Resized Image
st.title("Resized Image")
st.image(resized_image)