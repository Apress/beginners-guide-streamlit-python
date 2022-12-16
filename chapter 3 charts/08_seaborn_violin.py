# Import python libraries
import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data Set
df = pd.read_csv("./files/avocado.csv")

# Defining Violin Graph
fig = plt.figure(figsize=(10, 5))
sns.violinplot(x = "year", y="AveragePrice", data = df)
st.pyplot(fig)