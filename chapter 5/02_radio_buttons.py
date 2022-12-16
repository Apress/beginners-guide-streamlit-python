import streamlit as st

st.title('Creating Radio Buttons')

# Defining Radio Button
gender = st.radio(
    "Select your Gender",
    ('Male', 'Female', 'Others'))

if gender == 'Male':
    st.write('You have selected Male.')
elif gender == 'Female':
    st.write("You have selected Female.")
else:
    st.write("You have selected Others.")
