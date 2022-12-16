import streamlit as st

st.title('Session State')

# Session state initialization
if 'sum' not in st.session_state:
	st.session_state.sum = 0

# Button to add value
add = st.button('Add One')
if add:
    st.session_state.sum += 1

st.write('Total Sum = ', st.session_state.sum)