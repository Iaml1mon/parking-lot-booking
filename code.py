import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Title
st.title("🚗 Parking Lot Booking System")
st.subheader("Book your parking spot in seconds")

# Dummy locations
locations = ["Sydney CBD", "Parramatta", "Airport Parking", "Westfield Mall"]

# Form Input
with st.form("booking_form"):
    name = st.text_input("Your Name")
    location = st.selectbox("Select Parking Location", locations)
    date = st.date_input("Select Date", min_value=datetime.today())
    time = st.time_input("Select Time")
    submit = st.form_submit_button("Book Slot")

# Dummy bookings list
if 'bookings' not in st.session_state:
    st.session_state.bookings = []

# Handle submission
if submit and name:
    booking_info = {
        "Name": name,
        "Location": location,
        "Date": date.strftime("%Y-%m-%d"),
        "Time": time.strftime("%H:%M")
    }
    st.session_state.bookings.append(booking_info)
    st.success(f"✅ Slot booked successfully for {name} at {location} on {date} at {time}!")

# Show current bookings
df = pd.DataFrame(st.session_state.bookings)
if not df.empty:
    st.markdown("### 📋 Your Bookings")
    st.dataframe(df)
else:
    st.info("No bookings yet. Fill the form above to get started!")
