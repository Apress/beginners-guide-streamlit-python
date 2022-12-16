import streamlit as st

st.title("Download Button")

# Creating Download Button
down_btn = st.download_button(
        label="Download Image",
        data=open("./files/fam.jpg", "rb"),
        file_name="lions.jpg",
        mime="image/jpg"
    )
