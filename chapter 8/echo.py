import streamlit as st
import pandas as pd

st.title("Echo")
with st.echo():
    txt = st.text_input('Text')
    if not txt:
        st.warning('Input a text to see sample code.')
        st.stop()
    st.success('Thank you for text input.')
