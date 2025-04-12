import streamlit as st
import pandas as pd
from datetime import datetime

# Config
st.set_page_config(page_title="Smart Parking", layout="centered")

# Style
st.markdown("""
    <style>
    .main-title {
        font-size: 38px;
        font-weight: 700;
        color: #2E86C1;
        text-align: center;
        margin-bottom: 0px;
    }
    .sub-title {
        font-size: 18px;
        color: #5D6D7E;
        text-align: center;
        margin-bottom: 25px;
    }
    .stButton > button {
        background-color: #2E86C1;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 24px;
        font-size: 16px;
    }
    .stButton > button:hover {
        background-color: #1B4F72;
        color: #fff;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-title">🅿️ Smart Parking Booking System</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Reserve your parking slot instantly</div>', unsafe_allow_html=True)

# Booking form
st.markdown("## 📌 Book a Slot")

col1, col2 = st.columns(2)
with col1:
    location = st.selectbox("Select Location", ["Sydney CBD", "Parramatta", "Chatswood", "Homebush"])
with col2:
    date = st.date_input("Choose Date", datetime.today())

col3, col4 = st.columns(2)
with col3:
    time = st.time_input("Choose Time", datetime.now().time())
with col4:
    plate = st.text_input("Car Number Plate", max_chars=10, placeholder="e.g. ABC123")

booked = st.button("📥 Book Now")

# Booking Logic
if booked and plate:
    st.success(f"✅ Booking Confirmed for `{plate}` at **{location}** on **{date}** at **{time.strftime('%I:%M %p')}**")
    if "bookings" not in st.session_state:
        st.session_state.bookings = []
    st.session_state.bookings.append({
        "Location": location,
        "Date": date,
        "Time": time.strftime("%I:%M %p"),
        "Plate": plate
    })
elif booked and not plate:
    st.warning("⚠️ Please enter your car number plate.")

# Show bookings
st.markdown("## 📋 Your Recent Bookings")
if "bookings" in st.session_state and st.session_state.bookings:
    df = pd.DataFrame(st.session_state.bookings)
    st.dataframe(df, use_container_width=True)
else:
    st.info("No bookings yet.")

# Footer
st.markdown("---")
st.markdown("💡 *Powered by Streamlit | Developed for BISY2001 Project*", unsafe_allow_html=True)
