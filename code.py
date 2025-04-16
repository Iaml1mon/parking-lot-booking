import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Smart Parking", layout="wide")

# --- Configuration ---
locations = {
    "Sydney CBD": {"rate": 8.0, "slots": 20},
    "Parramatta": {"rate": 5.5, "slots": 15},
    "Chatswood": {"rate": 6.0, "slots": 10},
    "Homebush": {"rate": 4.0, "slots": 8},
}

ROWS, COLS = 4, 5

# --- Session State Setup ---
if "bookings" not in st.session_state:
    st.session_state.bookings = []

if "selected_slot" not in st.session_state:
    st.session_state.selected_slot = None

if "slot_data" not in st.session_state:
    st.session_state.slot_data = {
        loc: {"booked": [], "total": locations[loc]["slots"]}
        for loc in locations
    }

# --- Sidebar Booking Form ---
with st.sidebar:
    st.header("📌 Book Your Parking")
    location = st.selectbox("Choose Location", list(locations.keys()))
    rate = locations[location]["rate"]
    total_slots = locations[location]["slots"]
    booked_slots = len(st.session_state.slot_data[location]["booked"])
    available_slots = total_slots - booked_slots

    plate = st.text_input("Car Plate Number", max_chars=10)
    duration = st.slider("Parking Duration (hrs)", 1, 8, 2)
    date = st.date_input("Date", datetime.today())

    st.markdown(f"**💸 Rate/hr:** ${rate}  \n**🚗 Slots Available:** {available_slots}/{total_slots}")

# --- Grid UI ---
st.title("🅿️ Smart Parking Slot Booking")
st.subheader(f"📍 {location} Parking Slots")

slot_no = 1
for r in range(ROWS):
    cols = st.columns(COLS)
    for col in cols:
        if slot_no > locations[location]["slots"]:
            col.empty()
            continue

        slot_id = f"P{slot_no}"
        if slot_id in st.session_state.slot_data[location]["booked"]:
            col.button(f"❌ {slot_id}", key=f"{location}_{slot_id}", disabled=True)
        else:
            if col.button(f"🟩 {slot_id}", key=f"{location}_{slot_id}"):
                st.session_state.selected_slot = slot_id
        slot_no += 1

# --- Confirm Booking ---
if st.session_state.selected_slot:
    st.success(f"✅ Selected Slot: {st.session_state.selected_slot}")
    if st.button("📥 Confirm Booking"):
        if plate.strip() == "":
            st.warning("Please enter your car plate.")
        else:
            slot = st.session_state.selected_slot
            st.session_state.slot_data[location]["booked"].append(slot)
            total = rate * duration
            st.session_state.bookings.append({
                "Plate": plate.upper(),
                "Location": location,
                "Slot": slot,
                "Date": date.strftime("%Y-%m-%d"),
                "Hours": duration,
                "Rate/hr": f"${rate:.2f}",
                "Total": f"${total:.2f}"
            })
            st.success(f"🎉 Booking Confirmed for {plate.upper()} at {location}, Slot {slot}")
            st.session_state.selected_slot = None

# --- Booking Table ---
st.subheader("📋 Booking Summary")
if st.session_state.bookings:
    df = pd.DataFrame(st.session_state.bookings)
    st.dataframe(df, use_container_width=True)
else:
    st.info("No bookings yet.")

# --- Reset Option ---
with st.sidebar:
    if st.button("🔄 Reset All Bookings"):
        for loc in st.session_state.slot_data:
            st.session_state.slot_data[loc]["booked"] = []
        st.session_state.bookings = []
        st.success("System reset complete.")
