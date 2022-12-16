import streamlit as st

st.title("Text Box")

# Creating Text box with 10 as character limit
name = st.text_input("Enter your Name", max_chars=10)

st.write("Your Name is ", name)
