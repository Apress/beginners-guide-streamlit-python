import streamlit as st
import pandas as pd

st.title("CSV Data")
data_file = st.file_uploader("Upload CSV",type=["csv"])


details = st.button("Check Details")
if details:

    if data_file is not None:

        file_details = {"file_name":data_file.name, "file_type":data_file.type,
                        "file_size":data_file.size}
        
        st.write(file_details)
        df = pd.read_csv(data_file)
        st.dataframe(df)
    else:
        st.write("No CSV File is Uploaded")