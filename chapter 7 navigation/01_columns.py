import streamlit as st

#Defining Columns
col1, col2 = st.columns(2)

# Inserting Elements in column 1
col1.write("First Column")
col1.image("files/fam.jpg")

# Inserting Elements in column 2
col2.write("Second Column")
col2.image("files/fam.jpg")
