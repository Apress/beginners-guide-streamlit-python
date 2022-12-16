import streamlit as st
import plotly.graph_objects as go
import pandas as pd

#Read Avocado Dataset
data = pd.read_csv("./files/avocado.csv")

st.header("Pie Chart")

# Implementing Pie Plot
pie_chart = go.Figure(
    go.Pie(
    labels = data.type,
    values = data.AveragePrice,
    hoverinfo = "label+percent",
    textinfo = "value+percent"
))

st.plotly_chart(pie_chart)
