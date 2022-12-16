import streamlit as st

# Sidebar
st.sidebar.title("Sidebar")
st.sidebar.radio("Are you a New User", ["Yes", "No"])
st.sidebar.slider("Select a Number", 0,10)
