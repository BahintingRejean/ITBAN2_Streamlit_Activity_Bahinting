import streamlit as st
import pandas as pd

# Title and Description
st.title("CSV File Uploader & Filter")
st.write("Upload your CSV file and filter the data based on column values.")

# Sidebar for file upload and filtering options
st.sidebar.header("Upload CSV and Filter")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

# Process the uploaded file
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Display data preview
    st.subheader("Data Preview")
    st.dataframe(df.head())  # Show first few rows of the dataframe

    # Checkbox for showing raw data
    show_raw_data = st.sidebar.checkbox("Show Raw Data")
    if show_raw_data:
        st.subheader("Raw Data")
        st.write(df)

    # Filter Section
    st.sidebar.subheader("Filter Data")
    columns = df.columns.tolist()

    # Select column to filter by
    column_to_filter = st.sidebar.selectbox("Select column to filter", columns)

    # Get unique values for the selected column
    unique_values = df[column_to_filter].unique()
    selected_value = st.sidebar.selectbox(f"Select value to filter by in {column_to_filter}", unique_values)

    # Apply the filter
    filtered_df = df[df[column_to_filter] == selected_value]

    # Display filtered data
    st.subheader(f"Filtered Data: {column_to_filter} = {selected_value}")
    st.dataframe(filtered_df)

    # Option to download filtered data as a new CSV file
    st.sidebar.subheader("Download Filtered Data")
    csv = filtered_df.to_csv(index=False)
    st.sidebar.download_button("Download Filtered CSV", csv, "filtered_data.csv")
