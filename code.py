import streamlit as st

# --- Setup ---
st.set_page_config(page_title="Smart Parking Grid", layout="centered")

# --- Constants ---
TOTAL_SLOTS = 20
ROWS = 4
COLS = 5

# --- Initialize state ---
if "booked" not in st.session_state:
    st.session_state.booked = []

if "selected" not in st.session_state:
    st.session_state.selected = None

st.title("🅿️ Parking Slot Selection (Visual Grid)")
st.caption("🟩 Available | ❌ Booked")

# --- Draw grid ---
slot = 1
for r in range(ROWS):
    cols = st.columns(COLS)
    for c in cols:
        slot_id = f"P{slot}"
        if slot_id in st.session_state.booked:
            c.button(f"❌ {slot_id}", key=slot_id, disabled=True)
        else:
            if c.button(f"🟩 {slot_id}", key=slot_id):
                st.session_state.selected = slot_id
        slot += 1

# --- Booking Confirmation ---
if st.session_state.selected:
    st.success(f"✅ Selected: {st.session_state.selected}")
    if st.button("📥 Confirm Booking"):
        st.session_state.booked.append(st.session_state.selected)
        st.success(f"🎉 Slot {st.session_state.selected} booked successfully!")
        st.session_state.selected = None

# --- Booking list ---
if st.session_state.booked:
    st.subheader("📋 Booked Slots")
    st.write(", ".join(st.session_state.booked))

# --- Reset (for demo/test) ---
if st.button("🔄 Reset All"):
    st.session_state.booked = []
    st.session_state.selected = None
    st.success("Bookings reset!")
