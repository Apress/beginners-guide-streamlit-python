import streamlit as st

# CSV Download Button
st.title("Download Button")st.download_button(
     label="Download CSV",
     data=open("./files/avocado.csv", "rb"),
     file_name='data.csv',
     mime='csv',
 )
