import streamlit as st
import datetime

st.title("Date")

# Defining Time Function
st.date_input("Select Your Date", value=datetime.date(1989, 12, 25),
    min_value=datetime.date(1987, 1, 1),
    max_value=datetime.date(2005, 12, 1))

# st.write(age)