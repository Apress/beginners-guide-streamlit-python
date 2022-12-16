import streamlit as st

st.title('Creating Dropdown')

# Creating Dropdown
# hobby = st.selectbox('Choose your hobby: ', 
#         ('Books', 'Movies', 'Sports'))


hobby = st.selectbox('Choose your hobby: ', 
        ('Books', 'Movies', 'Sports'), 
        index=1)