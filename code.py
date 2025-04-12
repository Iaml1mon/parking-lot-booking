import streamlit as st
import pandas as pd
from datetime import datetime

# --- Config ---
st.set_page_config(page_title="Smart Parking", layout="centered")

# --- Styling ---
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
    .section-title {
        font-size: 22px;
        font-weight: bold;
        color: #117A65;
        margin-top: 40px;
        margin-bottom: 10px;
    }
    .prototype-box {
        background-color: #F2F3F4;
        padding: 20px;
        border-radius: 10px;
        font-family: monospace;
        font-size: 14px;
        margin-bottom: 20px;
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

# --- Header ---
st.markdown('<div class="main-title">🅿️ Smart Parking Booking System</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Reserve your parking slot instantly</div>', unsafe_allow_html=True)

# --- Booking Form ---
st.markdown('<div class="section-title">📌 Book a Slot</div>', unsafe_allow_html=True)
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

# --- Booking Logic ---
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

# --- Show Bookings ---
st.markdown('<div class="section-title">📋 Your Recent Bookings</div>', unsafe_allow_html=True)
if "bookings" in st.session_state and st.session_state.bookings:
    df = pd.DataFrame(st.session_state.bookings)
    st.dataframe(df, use_container_width=True)
else:
    st.info("No bookings yet.")

# --- Design Thinking ---
st.markdown('<div class="section-title">🧠 Design Thinking Process</div>', unsafe_allow_html=True)
st.markdown("""
- **Empathize**: Drivers struggle to find parking in busy areas.  
- **Define**: There’s no simple way to check real-time availability or reserve parking.  
- **Ideate**: A web app where users can select a place, date, time, and book easily.  
- **Prototype**: This app was built using Streamlit + Python + Pandas.  
- **Test**: Bookings confirmed, saved, and displayed in a clean dashboard view.
""")

# --- Features ---
st.markdown('<div class="section-title">📌 Key Features</div>', unsafe_allow_html=True)
st.markdown("""
- 📍 Location selector  
- 📅 Date & time picker  
- 🚘 Car plate input  
- ✅ Booking confirmation  
- 📊 Booking history table
""")

# --- SWOT ---
st.markdown('<div class="section-title">📊 SWOT Analysis</div>', unsafe_allow_html=True)
st.markdown("""
- **Strengths**: Simple UI, fast deployment, low cost  
- **Weaknesses**: No real-time slot data yet  
- **Opportunities**: Add QR codes, payments, or real GPS slots  
