import streamlit as st
import numpy as np

st.title("Container")

with st.container():
   st.write("Element Inside Contianer")

   # Defining Chart Element
   st.line_chart(np.random.randn(40, 4))

st.write("Element Outside Container")

