import streamlit as st

# Open Video using filepath with filename and read the video file
sample_video = open("files/ocean.mp4", "rb").read()

# Display Video using st.video() function
st.video(sample_video, start_time = 10)

st.write("Video Courtesy: https://filesamples.com/formats/mp4")