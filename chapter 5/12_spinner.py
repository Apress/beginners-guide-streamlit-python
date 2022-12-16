import streamlit as st
import time

st.title('Spinner')

# Defining Spinner
with st.spinner('Loading...'):
    time.sleep(5)
st.write('Hello Data Scientists')