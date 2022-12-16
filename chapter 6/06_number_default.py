import streamlit as st

# Create number input
num = st.number_input("Enter your Number", 0, 10, 5, 2)

st.write("Min. Value is 0,  \n  Max. value is 10")

st.write("Default Value is 5,  \n  Step Size value is 2")

st.write("Total value after adding Number entered with step value is:", num)