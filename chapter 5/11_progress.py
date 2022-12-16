import streamlit as st
import time

st.title('Progress Bar')

# Defining Progress Bar
download = st.progress(0)

for percentage in range(100):
    time.sleep(0)
    download.progress(percentage+1)

st.write('Download Complete')

# st.button(label="My button", style="background-color: #DD3300; color:#eeffee; border-radius: 0.75rem;")

import streamlit as st
m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #0099ff;
    color:#ffffff;
}
div.stButton > button:on_click {
    background-color: ##FFFF00;
    color:#ff0000;
    }
</style>""", unsafe_allow_html=True)

b = st.button("CLICK ME")