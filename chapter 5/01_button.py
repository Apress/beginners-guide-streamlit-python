import streamlit as st

st.title('Creating a Button')

# Defining Button
button = st.button('Click Here')

if button:
    st.write('You have clicked the Button')
else:
     st.write('You have not clicked the Button')
