import streamlit as st

# Open Audio using filepath with filename 
sample_audio = open("files/audio.wav", "rb")

#Reading Audio File
audio_bytes = sample_audio.read()

# Display Audio using st.audio() function with start time set to 20
st.audio(sample_audio, start_time = 20)

# Printing Audio Courtesy
st.write("Audio Courtesy: https://file-examples.com/index.php/sample-audio-files/sample-wav-download/")
