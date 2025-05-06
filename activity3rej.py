import streamlit as st

# Page Configuration
st.set_page_config(page_title="Data Warehousing Guide", page_icon="📦", layout="wide")

# Sidebar for Navigation
st.sidebar.title("📚 Topics in Data Warehousing")
option = st.sidebar.selectbox(
    "Select a Topic", 
    (
        "Overview of Data Warehousing", 
        "ETL Process", 
        "Data Integration", 
        "Data Governance", 
        "Performance Optimization"
    )
)

# Introductory Expander
with st.expander("ℹ️ What is Data Warehousing and Enterprise Data Management?"):
    st.markdown("""
    **Data Warehousing** is the process of aggregating structured data from various sources to enable strategic analysis and decision-making.  
    **Enterprise Data Management (EDM)** involves the governance, quality, and availability of data throughout its lifecycle in an organization.
    """)

# Main Content Area with Layout
st.markdown("---")
if option == "Overview of Data Warehousing":
    st.markdown("## 🏢 Overview of Data Warehousing")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📦 What is a Data Warehouse?")
        st.write("""
        A Data Warehouse is a centralized system used to store and analyze historical data. It supports business intelligence 
        and decision-making processes through organized, query-optimized structures.
        """)
    
    with col2:
        st.markdown("### 🧩 Components of a Data Warehouse")
        st.markdown("""
        - **Data Sources**: Internal and external databases, applications.
        - **ETL Process**: Extraction, transformation, and loading of data.
        - **Data Marts**: Department-specific subsets of the data warehouse.
        """)

elif option == "ETL Process":
    st.markdown("## 🔄 ETL Process")
    st.write("""
    The **ETL** process (Extract, Transform, Load) is essential for feeding data into a warehouse:
    
    - 🟡 **Extract**: Pull data from various sources.
    - 🔵 **Transform**: Clean and reformat data for consistency.
    - 🟢 **Load**: Insert transformed data into the data warehouse.
    """)

elif option == "Data Integration":
    st.markdown("## 🔗 Data Integration Techniques")
    st.write("""
    Combine data from various sources to create a unified, trusted view:
    
    - 🔁 **Data Replication**: Duplicate data from source systems.
    - 🌐 **Data Federation**: Query across systems without centralizing.
    - ⚡ **Data Virtualization**: Provide real-time access to distributed data.
    """)

elif option == "Data Governance":
    st.markdown("## 🛡️ Data Governance")
    st.write("""
    Data governance ensures the reliability, security, and regulatory compliance of enterprise data:
    
    - ✔️ **Data Quality**: Ensure completeness and accuracy.
    - 🔐 **Data Security**: Protect against unauthorized access.
    - 📜 **Data Privacy**: Align with regulations like GDPR or HIPAA.
    """)

elif option == "Performance Optimization":
    st.markdown("## 🚀 Performance Optimization")
    st.write("""
    Improve query speed and efficiency in a data warehouse:
    
    - 📌 **Indexing**: Faster lookup on key columns.
    - 📂 **Partitioning**: Organize data into manageable chunks.
    - 🧠 **Query Optimization**: Refine query logic and use caching.
    """)

# Additional Tabs
st.markdown("---")
st.markdown("### 📚 Additional Topics")
tab1, tab2, tab3 = st.tabs(["📈 Real-Time Analytics", "☁️ Cloud Data Warehousing", "🗄️ Data Archiving"])

with tab1:
    st.subheader("Real-Time Analytics")
    st.write("""
    Real-time analytics enables organizations to analyze data as it's ingested. It’s vital for time-sensitive decisions such as fraud detection or dynamic pricing.
    """)

with tab2:
    st.subheader("Cloud Data Warehousing")
    st.write("""
    Cloud solutions like Snowflake, BigQuery, and Redshift offer scalable and flexible infrastructure for modern data warehousing needs.
    """)

with tab3:
    st.subheader("Data Archiving")
    st.write("""
    Archiving allows long-term storage of infrequently accessed data, ensuring compliance and performance efficiency in active datasets.
    """)

# Footer
st.markdown("---")
st.markdown("<div style='text-align:center; color:gray;'>Crafted with 🧠 and ☁️ using Streamlit</div>", unsafe_allow_html=True)
