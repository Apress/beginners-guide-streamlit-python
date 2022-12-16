import streamlit as st

sub_form = st.form(key='submit_form')
user_name = sub_form.text_input('Enter your username')

# Submit button associated with form
submit_button = sub_form.form_submit_button('Submit')

st.write('Press submit see username displayed below')

if submit_button:
    st.write(f'Hello!!!! {user_name}')