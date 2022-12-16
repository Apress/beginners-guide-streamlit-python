import streamlit as st
import time

st.title('Hello World')
st.info('Script Runs Everytime rerun hits.')
time.sleep(2)

# rerun statement
st.experimental_rerun()
st.success('Scipt Never Runs.')  