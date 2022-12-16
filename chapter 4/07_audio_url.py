import streamlit as st

# Open Audio using filepath with filename and read the audio file
sample_url = st.audio("https://www.learningcontainer.com/wp-content/uploads/2020/02/Kalimba.mp3")

st.write("Audio Courtesy: https://www.learningcontainer.com/sample-audio-file/")
