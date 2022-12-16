import streamlit as st
import time

# Empty Container
with st.empty():
    for seconds in range(5):
        st.write(f"⏳ {seconds} seconds have passed")
        time.sleep(1)
    st.write("✔️ Times up!")