import streamlit as st

# Creating Text Area
input_text = st.text_area("Enter your Review")

# Printing entered text
st.write("""You entered:  \n""",input_text)
