import streamlit as st
import cv2
import numpy as np
from datetime import datetime

st.set_page_config(page_title="Real-Time Video Filter", layout="wide")

# --- App Header ---
st.title("🎥 Real-Time Video Stream with Filters")
st.markdown("""
Welcome to the **Streamlit + OpenCV** video processing demo. Select filters from the sidebar to modify the live webcam feed in real time.
""")

# --- Sidebar Controls ---
st.sidebar.header("⚙️ Controls")
filter_type = st.sidebar.radio("Choose a filter", ["None", "Grayscale", "Canny Edge", "Face Detection"])

# Thresholds for Canny filter (only show if selected)
if filter_type == "Canny Edge":
    st.sidebar.subheader("Canny Thresholds")
    low_threshold = st.sidebar.slider("Low Threshold", 0, 100, 30)
    high_threshold = st.sidebar.slider("High Threshold", 100, 300, 150)
else:
    low_threshold = high_threshold = None

take_snapshot = st.sidebar.button("📸 Take Snapshot")

# Load face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Initialize camera
cap = cv2.VideoCapture(0)
FRAME_WINDOW = st.empty()
snapshot_container = st.container()

# Main loop
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        st.error("🚫 Unable to access webcam.")
        break

    # Apply filter
    if filter_type == "Grayscale":
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)

    elif filter_type == "Canny Edge":
        edges = cv2.Canny(frame, low_threshold, high_threshold)
        frame = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)

    elif filter_type == "Face Detection":
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display frame in Streamlit
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame_rgb, channels="RGB")

    # Snapshot functionality
    if take_snapshot:
        filename = f"snapshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
        cv2.imwrite(filename, frame)
        with snapshot_container:
            st.success(f"📷 Snapshot saved: `{filename}`")
            st.image(frame_rgb, caption="Snapshot", use_column_width=True)
        break

cap.release()
