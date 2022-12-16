import streamlit as st
import pandas as pd
import numpy as np

st.title("Experimental Show for Debugging")
# Dataframe
df = pd.DataFrame(np.random.randint(0,100,size=(5, 4)), columns=list('WXYZ'))

# Defining Experimental show
st.experimental_show(df)
