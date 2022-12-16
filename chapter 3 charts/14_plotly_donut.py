import streamlit as st
import pandas as pd
import plotly.express as px

#Read Avocado Dataset
data = pd.read_csv("./files/avocado.csv")

st.header("Donut Chart")

# Donut Chart
donut_chart = px.pie(
    names = data.type,
    values = data.AveragePrice,
    hole=0.25,
)

st.plotly_chart(donut_chart)