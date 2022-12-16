import streamlit as st
import pandas as pd
import numpy as np

st.title('Map')

# Defining Latitude and Longitude 
locate_map = pd.DataFrame(
  np.random.randn(50, 2)/[10,10] + [15.4589, 75.0078],
  columns = ['latitude', 'longitude'])

# Map Function
st.map(locate_map)
