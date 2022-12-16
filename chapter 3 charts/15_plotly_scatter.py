import streamlit as st
import pandas as pd
import plotly.express as px

#Data Set
data = pd.read_csv("./files/avocado.csv")

st.header("Scatter Chart")

#Scatter
scat = px.scatter(
    x = data.Date,
    y = data.AveragePrice
)

st.plotly_chart(scat)