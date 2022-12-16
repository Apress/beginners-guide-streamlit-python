import streamlit as st
import pandas as pd
import plotly.express as px

# Data Set
data = pd.read_csv("./files/avocado.csv")

# Minimizing Dataset
albany_df = data[data['region']=="Albany"]
al_df = albany_df[albany_df["year"]==2015]

# Horizontal Bar
bar_graph = px.bar(
    al_df,
    x = "Large Bags",
    y = "Date",
    title = "Bar Graph",
    color="Large Bags",
    orientation='h'
)