import streamlit as st

st.title("Multi-Select")

# Defining Multi_Select with No Pre-Selection
hobbies = st.multiselect(
    'What are your Hobbies',
    ['Reading', 'Cooking', 'Watching Movies/TV Series', 'Playing', 'Drawing', 'Hiking'])