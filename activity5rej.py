import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text

# --- Configuration ---
DB_USER = 'root'
DB_PASSWORD = None
DB_HOST = 'localhost'
DB_PORT = '3306'
DB_NAME = 'school_system'

# --- MySQL Connection ---
@st.cache_resource
def get_connection():
    if DB_PASSWORD is None:
        connection_url = f"mysql+pymysql://{DB_USER}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    else:
        connection_url = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    return create_engine(connection_url)

engine = get_connection()

# --- Login Sidebar ---
st.sidebar.title("🔐 Admin Login")
username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

def authenticate(user, pwd):
    return user == "admin" and pwd == "school123"

# --- Main Interface ---
if authenticate(username, password):
    st.success(f"Welcome, {username}!")
    st.title("🎓 Student Enrollment Dashboard")
    st.markdown("Manage student and course records from the database below.")

    # --- Table Selection ---
    table_name = st.selectbox("📁 Select Table", ["students", "courses"])

    # --- Filter & View Records ---
    st.subheader(f"📄 View `{table_name}` Records")
    st.markdown("Use the filter field to add custom SQL WHERE conditions (e.g., `year_level = '2'`).")
    filter_query = st.text_input("SQL Filter")

    query = f"SELECT * FROM {table_name}"
    if filter_query.strip():
        query += f" WHERE {filter_query}"

    with engine.connect() as conn:
        result_df = pd.read_sql(text(query), conn)

    st.dataframe(result_df, use_container_width=True)

    st.markdown("---")

    # --- Insert New Record ---
    st.subheader(f"➕ Add New Record to `{table_name}`")
    with st.form(key='insert_form', border=True):
        if table_name == 'students':
            col1, col2 = st.columns(2)
            with col1:
                full_name = st.text_input("Full Name")
            with col2:
                year_level = st.selectbox("Year Level", ["1", "2", "3", "4"])
            course = st.text_input("Course")
            submit = st.form_submit_button("📥 Insert Student")

            if submit and full_name and course:
                insert_query = text("""
                    INSERT INTO students (full_name, year_level, course)
                    VALUES (:name, :year, :course)
                """)
                with engine.connect() as conn:
                    conn.execute(insert_query, {"name": full_name, "year": year_level, "course": course})
                    conn.commit()
                st.success("✅ Student record inserted!")
            elif submit:
                st.warning("⚠️ Please fill in all fields.")

        elif table_name == 'courses':
            col1, col2 = st.columns(2)
            with col1:
                course_name = st.text_input("Course Name")
            with col2:
                course_code = st.text_input("Course Code")
            submit = st.form_submit_button("📥 Insert Course")

            if submit and course_name and course_code:
                insert_query = text("""
                    INSERT INTO courses (course_name, course_code)
                    VALUES (:name, :code)
                """)
                with engine.connect() as conn:
                    conn.execute(insert_query, {"name": course_name, "code": course_code})
                    conn.commit()
                st.success("✅ Course added!")
            elif submit:
                st.warning("⚠️ Please fill in all fields.")
else:
    st.warning("🔒 Please log in with valid credentials to access the dashboard.")
