import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from streamlit_extras.colored_header import colored_header

# Page Config
st.set_page_config(page_title="🚗 Parking Lot Booking", page_icon="🅿️", layout="centered")

# Header with Style
colored_header(label="Smart Parking Lot Booking System", description="Book your parking slot hassle-free.", color_name="blue-green-70")
st.markdown("""
<style>
    .main {
        background-color: #f1f3f6;
        font-family: 'Segoe UI', sans-serif;
    }
    .stButton>button {
        background-color: #007bff;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
    }
    .stTextInput>div>div>input {
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

# Dummy locations
locations = ["Sydney CBD", "Parramatta", "Airport Parking", "Westfield Mall"]

# Form Card
with st.container():
    st.markdown("## 📋 Book a Parking Slot")
    with st.form("booking_form"):
        name = st.text_input("👤 Your Full Name")
        location = st.selectbox("📍 Choose Location", locations)
        date = st.date_input("📅 Select Date", min_value=datetime.today())
        time = st.time_input("⏰ Choose Time")
        submitted = st.form_submit_button("🚘 Book Now")

# Booking Logic
if 'bookings' not in st.session_state:
    st.session_state.bookings = []

if submitted and name:
    new_booking = {
        "👤 Name": name,
        "📍 Location": location,
        "📅 Date": date.strftime("%Y-%m-%d"),
        "⏰ Time": time.strftime("%H:%M")
    }
    st.session_state.bookings.append(new_booking)
    st.success(f"✅ Parking slot successfully booked at {location} on {date.strftime('%d %b %Y')} at {time.strftime('%I:%M %p')}.")

# Show Booking Table
if st.session_state.bookings:
    st.markdown("---")
    st.markdown("## 📊 Booking History")
    df = pd.DataFrame(st.session_state.bookings)
    st.dataframe(df, use_container_width=True)
else:
    st.markdown("---")
    st.info("No bookings made yet. Fill the form above to secure a spot! 🚗")
