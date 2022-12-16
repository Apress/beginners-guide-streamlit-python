import altair as alt
import streamlit as st
import pandas as pd

#Read albany Dataset
df = pd.read_csv("./files/albany.csv")

# Box Plot
box_plot = alt.Chart(df).mark_boxplot().encode(
    x = "Date",
    y = "Large Bags"
)

st.altair_chart(box_plot)