from re import X
from tkinter import Y
import streamlit as st
import time

# Defining cache
@st.cache

def add(x, y):
    # Function takes 5 secs to run 
    time.sleep(5)  
    return x + y

x = 10
y = 60
res = add(x, y)

st.write("Result:", res)