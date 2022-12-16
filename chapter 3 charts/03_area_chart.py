import streamlit as st
import pandas as pd
import numpy as np

st.title('Area')

# Defining dataframe with its values 
df = pd.DataFrame(
    np.random.randn(40, 4),
    columns=["C1", "C2", "C3", "C4"])

# Bar Chart 
st.area_chart(df)
