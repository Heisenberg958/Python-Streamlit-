import csv
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# st.write("Hello World")
# st.write({"Key":["Value"]})

st.title("Simple Data Dashboard")
uploaded_file=st.file_uploader("Choose A CSV File ",type="csv")

if uploaded_file is not None:
    # st.write("File Uploaded....")
    df=pd.read_csv(uploaded_file)
    st.subheader("Data Preview")
    st.write(df.head())


    st.subheader("Data Summary")
    st.write(df.describe())


    st.subheader("Filter Data")
    columns=df.columns.tolist()
    selected_column=st.selectbox("Select Columns to filter by ",columns)


    unique_values=df[selected_column].unique()
    selected_values=st.selectbox("Select Values",unique_values)


    filter_df=df[df[selected_column]==selected_values]
    st.write(filter_df)


    st.subheader("Plot Data")
    x_column=st.selectbox("Select X-axis column",columns)
    y_column=st.selectbox("Select Y-axis column",columns)


    if st.button("Generate Plot/Chart "):
        st.line_chart(filter_df.set_index(x_column)[y_column])
else:
    st.write("Waiting File To Upload")
