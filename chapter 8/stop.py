import streamlit as st

name = st.text_input('Text')
if not name:
  st.info('Enter any Text.')
  # Stop function
  st.stop()
st.success('Text Entered Successfully.')  