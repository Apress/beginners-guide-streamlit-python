import streamlit as st

# Image Courtesy
st.write("Siplaying Multiple Images")

# Listing out animal images
animal_images = [
    'files/animal1.jpg',
    'files/animal2.jpg',
    'files/animal3.jpg',
    'files/animal4.jpg',
    'files/animal5.jpg',
    'files/animal6.jpg',
    'files/animal7.jpg',
    'files/animal8.jpg',
    'files/animal9.jpg',
    'files/animal10.jpg'
   
]

# Displaying Multiple images with width 150
st.image(animal_images, width=150)

# Image Courtesy
st.write("Image Courtesy: Unplash")