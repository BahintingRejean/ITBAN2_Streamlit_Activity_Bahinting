
![image alt](https://github.com/BahintingRejean/ITBAN2_Streamlit_Activity_Bahinting/blob/baf89c8ae4d4b1eeee03ccf7b17b34a5f100e86d/Screenshot%20(211).png)

![image alt](https://github.com/BahintingRejean/ITBAN2_Streamlit_Activity_Bahinting/blob/9cda7678069ff5ee57cc2439c1f1243ef816d48f/Activity1.png)

Task 1

In task 1, I started importing the necessary library, like streamlit as st. It displays a welcoming title, header, and a brief description to orient the user. It then collects user input through several fields: email, a masked PIN (for privacy), full name, address, and age (restricted between 1 and 100 for validation). These inputs are created using st.text_input for text and st.number_input for the numeric age field. After the user enters their details, the app immediately reflects the information back using st.write, adding emojis for a more user-friendly and visually appealing output.



Task 2

In task 2, the users can enable uploading any CSV file or a dataset. It begins with a title and brief description, then utilizes the sidebar for file upload via st.sidebar.file_uploader. After a file is uploaded, the app reads the data using pandas and shows a preview of the first few rows with st.dataframe(df.head()). There's also an option to display the complete dataset using a checkbox. For filtering, users can choose a column from a dropdown list and then select a specific value within that column to filter the data. The resulting filtered dataset is displayed on the main screen and can be downloaded as a new CSV file through st.sidebar.download_button, providing a simple and interactive way to explore and extract data without needing to write any code.



Task 3

This task serves as an interactive guide about data warehousing and enterprise data management and related topics. It features a sidebar menu that allows users to select topics like ETL, Data Integration, and Performance Optimization, with each section dynamically displaying relevant explanations. An expandable section gives a quick overview of data warehousing and enterprise data management. Additional learning content is provided through tabs on real-time analytics, cloud data warehousing, and data archiving.

Task 4

In this task 4 , it shows the data dashboard of COVID-19 that allows users to select a country from a dropdown menu (st.selectbox) and view the past 30 days of pandemic trends. After setting up the page layout and title, it shows the historical COVID-19 data from the public API disease.sh using the selected country. If the API request is successful and contains a "timeline," the data for cases, deaths, and recoveries is extracted and converted into a pandas DataFrame with a datetime index. Summary statistics for total cases, deaths, and recoveries are displayed at the top using metric widgets. The app then splits into two columns to show visualizations: line, area, pie, and bar charts for trends in cases, recoveries, and deaths, as well as a delta chart showing new daily cases. Finally, it displays a data table previewing the last 30 days, with error handling included in case of API issues.



Task 5

In task 5, it is designed to allow an admin to manage student and course records within a school system database. The app connects to a MySQL database using SQLAlchemy, and upon logging in via the sidebar with valid credentials, the admin can interact with student and course data. The app lets the admin view records from the selected table, with the ability to apply custom SQL filters. 



Task 6 



This Streamlit app creates a real-time video stream with various filter options using OpenCV, allowing users to apply filters such as Grayscale, Canny Edge, and Face Detection to a live webcam feed. The user can select a filter from the sidebar, and if the "Canny Edge" filter is chosen, they can adjust the threshold values for edge detection. The app also includes a snapshot feature, where users can capture a frame from the webcam feed, save it as an image file, and display it in the app. The webcam feed is processed frame-by-frame, applying the selected filter, and is continuously displayed using st.empty(). 
