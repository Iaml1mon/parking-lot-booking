import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Smart Parking Booking", layout="centered")

# --- Parking Config ---
locations = {
    "Sydney CBD": {"rate": 8.0, "slots": 20},
    "Parramatta": {"rate": 5.5, "slots": 15},
    "Chatswood": {"rate": 6.0, "slots": 10},
    "Homebush": {"rate": 4.0, "slots": 8},
}

ROWS, COLS = 4, 5

# --- State ---
if "bookings" not in st.session_state:
    st.session_state.bookings = []

if "selected_slot" not in st.session_state:
    st.session_state.selected_slot = None

if "slot_data" not in st.session_state:
    st.session_state.slot_data = {
        loc: {"booked": [], "total": locations[loc]["slots"]}
        for loc in locations
    }

# --- Page Title ---
st.title("🅿️ Smart Parking Booking System")
st.write("Inspired by Wilson Parking — Simple, Visual, Fast")

# --- Booking Form on Screen ---
st.subheader("📌 Book Your Spot")
col1, col2, col3 = st.columns(3)

with col1:
    location = st.selectbox("Choose Location", list(locations.keys()))
    rate = locations[location]["rate"]

with col2:
    plate = st.text_input("Car Plate Number", max_chars=10)

with col3:
    duration_input = st.text_input("Duration (hours)", placeholder="e.g. 2")

date = st.date_input("Booking Date", datetime.today())

available = locations[location]["slots"] - len(st.session_state.slot_data[location]["booked"])
st.write(f"💸 Rate/hr: ${rate} | 🚗 Available Slots: {available}/{locations[location]['slots']}")

# --- Visual Grid UI ---
st.subheader(f"🗺️ {location} Parking Layout")

slot_no = 1
for r in range(ROWS):
    cols = st.columns(COLS)
    for col in cols:
        if slot_no > locations[location]["slots"]:
            col.empty()
        else:
            slot_id = f"P{slot_no}"
            if slot_id in st.session_state.slot_data[location]["booked"]:
                col.button(f"❌ {slot_id}", key=f"{location}_{slot_id}", disabled=True)
            else:
                if col.button(f"🟩 {slot_id}", key=f"{location}_{slot_id}"):
                    st.session_state.selected_slot = slot_id
            slot_no += 1

# --- Confirm Booking ---
if st.session_state.selected_slot:
    st.success(f"Selected Slot: {st.session_state.selected_slot}")
    if st.button("📥 Confirm Booking"):
        if not plate.strip():
            st.warning("Enter a car plate.")
        elif not duration_input.isdigit():
            st.warning("Enter valid duration (1-8 hours).")
        else:
            duration = int(duration_input)
            total = rate * duration
            st.session_state.slot_data[location]["booked"].append(st.session_state.selected_slot)
            st.session_state.bookings.append({
                "Plate": plate.upper(),
                "Location": location,
                "Slot": st.session_state.selected_slot,
                "Date": date.strftime("%Y-%m-%d"),
                "Hours": duration,
                "Rate/hr": f"${rate:.2f}",
                "Total": f"${total:.2f}"
            })
            st.success(f"✅ Booking Confirmed for {plate.upper()} | Slot {st.session_state.selected_slot}")
            st.session_state.selected_slot = None

# --- Booking Table ---
st.subheader("📋 All Bookings")
if st.session_state.bookings:
    df = pd.DataFrame(st.session_state.bookings)
    st.dataframe(df, use_container_width=True)
else:
    st.info("No bookings yet.")

# --- Reset Button ---
if st.button("🔄 Reset All"):
    for loc in st.session_state.slot_data:
        st.session_state.slot_data[loc]["booked"] = []
    st.session_state.bookings = []
    st.success("All bookings have been reset.")
