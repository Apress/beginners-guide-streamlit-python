import streamlit as st

st.title("Text Box")

# Creating Text box
name = st.text_input("Enter your Name")

st.write("Your Name is ", name)