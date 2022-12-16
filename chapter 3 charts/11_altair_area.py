import altair as alt
import streamlit as st
import pandas as pd

#Read albany Dataset
df = pd.read_csv("./files/albany.csv")

# Area Plot
area = alt.Chart(df).mark_area(color="orange").encode(
    x = "Date",
    y = "Large Bags"
)

st.altair_chart(area)