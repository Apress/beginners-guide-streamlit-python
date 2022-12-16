import streamlit as st
from PIL import Image

img = Image.open("files/fam.jpg")

st.title("Padding")

# Defining Padding with columns
col1, padding, col2 = st.columns((10,2,10))

with col1:
    col1.image(img)

with col2:
    col2.image(img)
