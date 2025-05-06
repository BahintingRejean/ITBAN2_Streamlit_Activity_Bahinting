import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

# Page Setup
st.set_page_config(page_title="COVID-19 Dashboard", page_icon="🦠", layout="wide")
st.title("🌍 COVID-19 Data Dashboard")

# Country selection
country = st.selectbox("Choose a country", ["USA", "Philippines", "India", "Brazil", "Germany"])

# Fetch data
url = f"https://disease.sh/v3/covid-19/historical/{country}?lastdays=30"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    if 'timeline' in data:
        timeline = data['timeline']
        cases = pd.Series(timeline['cases'])
        deaths = pd.Series(timeline['deaths'])
        recovered = pd.Series(timeline['recovered'])

        df = pd.DataFrame({
            'Date': cases.index,
            'Cases': cases.values,
            'Deaths': deaths.values,
            'Recovered': recovered.values
        })
        df['Date'] = pd.to_datetime(df['Date'])
        df.set_index('Date', inplace=True)

        # Layout: Metrics at Top
        st.markdown("### 📊 Summary Statistics (Last 30 Days)")
        col1, col2, col3 = st.columns(3)
        col1.metric("🧪 Total Cases", f"{df['Cases'].iloc[-1]:,}")
        col2.metric("💀 Total Deaths", f"{df['Deaths'].iloc[-1]:,}")
        col3.metric("💚 Total Recovered", f"{df['Recovered'].iloc[-1]:,}")

        st.markdown("---")

        # Layout: Charts in 2 Columns
        col_left, col_right = st.columns(2)

        with col_left:
            st.subheader("📈 Line Chart - Daily Cases")
            st.line_chart(df['Cases'])

            st.subheader("📉 Area Chart - Daily Recovered")
            st.area_chart(df['Recovered'])

            st.subheader("📌 Pie Chart - Total Distribution")
            totals = {
                'Cases': df['Cases'].iloc[-1],
                'Deaths': df['Deaths'].iloc[-1],
                'Recovered': df['Recovered'].iloc[-1]
            }
            fig, ax = plt.subplots()
            ax.pie(totals.values(), labels=totals.keys(), autopct="%1.1f%%", startangle=90)
            ax.axis("equal")
            st.pyplot(fig)

        with col_right:
            st.subheader("📊 Bar Chart - Daily Deaths")
            st.bar_chart(df['Deaths'])

            st.subheader("🔁 Change in Cases (Delta)")
            df['New Cases'] = df['Cases'].diff().fillna(0)
            st.line_chart(df['New Cases'])

        st.markdown("---")
        st.markdown("📅 **Last 30 Days Data Preview**")
        st.dataframe(df.reset_index())

    else:
        st.error("No timeline data found.")
else:
    st.error(f"API request failed with status code {response.status_code}")
