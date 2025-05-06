import streamlit as st

st.title("HELLO, STREAMLIT")
st.header("STREAMLIT APP")
st.write("app demonstration")

# Input fields
email = st.text_input("Enter your email")
pin = st.text_input("Enter your digit PIN", type="password")
name = st.text_input("Enter your full name")
address = st.text_input("Enter your address")
age = st.number_input("Enter your age", min_value=1, max_value=100)

# Display what the user typed
st.write("📧 Your email is:", email)
st.write("🔢 Your PIN is:", pin)
st.write("👤 Your name is:", name)
st.write("🏠 Your address is:", address)
st.write("🎂 Your age is:", age)
