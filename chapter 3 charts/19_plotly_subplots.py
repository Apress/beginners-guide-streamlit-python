import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Data Set
data = pd.read_csv("./files/avocado.csv")

# Minimizing Dataset
albany_df = data[data['region']=="Albany"]
al_df = albany_df[albany_df["year"]==2015]

fig = make_subplots(rows=3, cols=1)

# First Subplot
fig.add_trace(go.Scatter(
    x=al_df["Date"],
    y=al_df["Total Bags"],
), row=1, col=1)

# Second SubPlot
fig.add_trace(go.Scatter(
    x=al_df["Date"],
    y=al_df["Small Bags"],
), row=2, col=1)

# Third SubPlot
fig.add_trace(go.Scatter(
   x=al_df["Date"],
   y=al_df["Large Bags"],
), row=3, col=1)

st.plotly_chart(fig)