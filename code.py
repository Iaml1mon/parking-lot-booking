import streamlit as st
import pandas as pd
from datetime import datetime
from PIL import Image

# --- Config ---
st.set_page_config(page_title="Wilson-style Parking App", layout="centered")

# --- Fake Data for Demo ---
location_data = {
    "Sydney CBD": {"rate": 8.0, "slots": 10, "map": "https://www.google.com/maps?q=sydney+CBD+parking&output=embed"},
    "Parramatta": {"rate": 5.5, "slots": 8, "map": "https://www.google.com/maps?q=parramatta+parking&output=embed"},
    "Chatswood": {"rate": 6.0, "slots": 7, "map": "https://www.google.com/maps?q=chatswood+parking&output=embed"},
    "Homebush": {"rate": 4.0, "slots": 5, "map": "https://www.google.com/maps?q=homebush+parking&output=embed"},
}

# --- Session state for bookings and slots ---
if "bookings" not in st.session_state:
    st.session_state.bookings = []

if "slots" not in st.session_state:
    st.session_state.slots = {loc: location_data[loc]["slots"] for loc in location_data}

# --- UI: Title ---
st.title("🅿️ Smart Parking Booking System")
st.caption("Inspired by Wilson Parking • With maps, slots & pricing")

# --- Booking Form ---
st.header("📌 Book Your Slot")

col1, col2 = st.columns(2)
with col1:
    location = st.selectbox("Select Location", list(location_data.keys()))
    rate = location_data[location]["rate"]
    slots_left = st.session_state.slots[location]
    st.markdown(f"**Available Slots:** {slots_left} 🚗")
with col2:
    plate = st.text_input("Car Number Plate", max_chars=10)

col3, col4 = st.columns(2)
with col3:
    date = st.date_input("Select Date", datetime.today())
with col4:
    duration = st.slider("Select Parking Duration (hours)", 1, 8, 2)

# --- Map View (Simple iframe) ---
st.markdown("### 🗺️ Location Map")
st.components.v1.iframe(location_data[location]["map"], width=700, height=300)

# --- Booking Logic ---
if st.button("📥 Confirm Booking"):
    if plate == "":
        st.warning("⚠️ Please enter your car number plate.")
    elif st.session_state.slots[location] <= 0:
        st.error("⛔ No more slots available at this location.")
    else:
        total = rate * duration
        st.session_state.bookings.append({
            "Location": location,
            "Date": date.strftime("%Y-%m-%d"),
            "Duration": duration,
            "Rate/hr": f"${rate:.2f}",
            "Total": f"${total:.2f}",
            "Plate": plate.upper()
        })
        st.session_state.slots[location] -= 1
        st.success(f"✅ Booking Confirmed for {plate.upper()}")
        st.info(f"📍 {location} | {duration} hrs | 💸 ${total:.2f}")
        st.caption("Save this as your booking receipt.")

# --- Booking Table ---
if st.session_state.bookings:
    st.subheader("📋 My Bookings")
    st.dataframe(pd.DataFrame(st.session_state.bookings), use_container_width=True)
else:
    st.info("No bookings yet.")

# --- Footer ---
st.markdown("---")
st.markdown("🚀 Built for BISY2001 | Wilson-Style Parking System | [Your Name]", unsafe_allow_html=True)
