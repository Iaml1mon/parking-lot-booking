import streamlit as st
import pandas as pd
from datetime import datetime, time

# --- Setup ---
st.set_page_config(page_title="Smart Parking App", layout="centered")
if "bookings" not in st.session_state:
    st.session_state.bookings = []

# --- Fake location data & rates ---
location_rates = {
    "Sydney CBD": 8.0,        # $8/hour
    "Parramatta": 5.5,        # $5.5/hour
    "Chatswood": 6.0,         # $6/hour
    "Homebush": 4.0           # $4/hour
}

# --- Title ---
st.title("🅿️ Smart Parking Booking System")
st.caption("Real-time booking + pricing")

# --- Booking Form ---
st.header("📌 Book Your Slot")
col1, col2 = st.columns(2)
with col1:
    location = st.selectbox("Select Location", list(location_rates.keys()))
    rate = location_rates[location]
with col2:
    plate = st.text_input("Car Number Plate", max_chars=10)

col3, col4 = st.columns(2)
with col3:
    date = st.date_input("Select Date", datetime.today())
with col4:
    duration = st.slider("Select Parking Duration (hours)", 1, 8, 2)

confirm = st.button("📥 Confirm Booking")

# --- Booking Logic ---
if confirm:
    if plate == "":
        st.warning("Please enter your car number plate.")
    else:
        price = duration * rate
        booking_data = {
            "Location": location,
            "Date": date.strftime("%Y-%m-%d"),
            "Duration (hr)": duration,
            "Rate/hr": f"${rate:.2f}",
            "Total Cost": f"${price:.2f}",
            "Plate": plate.upper()
        }
        st.session_state.bookings.append(booking_data)

        st.success("✅ Booking Confirmed!")
        st.info(f"📍 {location} | 🕒 {duration} hrs | 💸 ${price:.2f}")
        st.caption("Show this on entry as your booking receipt.")

# --- Booking History ---
if st.session_state.bookings:
    st.subheader("📋 My Bookings")
    df = pd.DataFrame(st.session_state.bookings)
    st.dataframe(df, use_container_width=True)
else:
    st.info("No bookings yet. Book a slot to get started.")

# --- Footer ---
st.markdown("---")
st.markdown("🚀 Built with Streamlit By Limon Sheikh", unsafe_allow_html=True)
