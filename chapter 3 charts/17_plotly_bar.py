import streamlit as st
import pandas as pd
import plotly.express as px

# Data Set
data = pd.read_csv("./files/avocado.csv")

# Minimizing Dataset
albany_df = data[data['region']=="Albany"]
al_df = albany_df[albany_df["year"]==2015]

# Bar graph
# bar_graph = px.bar(
#     al_df,
#     title = "Bar Graph",
#     x = "Date",
#     y = "Large Bags"
#     )

#Bar Color
# bar_graph = px.bar(
#     x = al_df["Date"],
#     y = al_df["Large Bags"],
#     title = "Bar Graph",
#     color=al_df["Large Bags"]
# )

# Horizontal Bar
bar_graph = px.bar(
    al_df,
    x = "Large Bags",
    y = "Date",
    title = "Bar Graph",
    color="Large Bags",
    orientation='h'
)



st.plotly_chart(bar_graph)