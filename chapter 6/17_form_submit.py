import streamlit as st

my_form = st.form(key='form')
my_form.text_input(label='Enter any text')

# Defining submit button
submit_button = my_form.form_submit_button(label='Submit')