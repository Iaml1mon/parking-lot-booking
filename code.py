import streamlit as st
import pandas as pd
from datetime import datetime

# --- Setup ---
st.set_page_config(page_title="Smart Parking Slide App", layout="centered")

if "slide" not in st.session_state:
    st.session_state.slide = 1

def next_slide():
    st.session_state.slide += 1

def prev_slide():
    st.session_state.slide -= 1

# --- Styling ---
st.markdown("""
    <style>
    .title { font-size: 38px; font-weight: 700; text-align: center; color: #2E86C1; }
    .subtitle { font-size: 18px; text-align: center; color: #5D6D7E; margin-bottom: 30px; }
    .section-title { font-size: 24px; font-weight: bold; margin-top: 20px; color: #117A65; }
    .box { background-color: #F2F3F4; padding: 20px; border-radius: 10px; margin-bottom: 20px; font-size: 16px; }
    .stButton > button {
        background-color: #2E86C1;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 8px 24px;
        font-size: 16px;
        margin: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Slides ---
slide = st.session_state.slide

if slide == 1:
    st.markdown('<div class="title">🅿️ Smart Parking Booking System</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">A presentation by [Your Name] | BISY2001 Assessment</div>', unsafe_allow_html=True)

elif slide == 2:
    st.markdown('<div class="section-title">🧠 Design Thinking Process</div>', unsafe_allow_html=True)
    st.markdown("""
    - **Empathize**: Drivers can’t find parking easily in crowded areas  
    - **Define**: No real-time way to book and view parking availability  
    - **Ideate**: A simple web app for booking slots  
    - **Prototype**: Built with Streamlit and Python  
    - **Test**: Confirmed bookings and history table
    """)

elif slide == 3:
    st.markdown('<div class="section-title">📊 SWOT Analysis</div>', unsafe_allow_html=True)
    st.markdown("""
    - **Strengths**: Simple UI, fast, easy to deploy  
    - **Weaknesses**: No real GPS/live data yet  
    - **Opportunities**: Add payments, QR codes, real-time slots  
    - **Threats**: Security & double-booking
    """)

elif slide == 4:
    st.markdown('<div class="section-title">🖼️ UI Prototypes</div>', unsafe_allow_html=True)
    st.markdown('<div class="box">🏠 Home Screen → Welcome, [Book Slot Now]</div>', unsafe_allow_html=True)
    st.markdown('<div class="box">🗓️ Booking Page → Select Location, Date, Time, Plate</div>', unsafe_allow_html=True)
    st.markdown('<div class="box">✅ Confirmation → “Booking Successful!”</div>', unsafe_allow_html=True)
    st.markdown('<div class="box">📋 Booking History Table → See past bookings</div>', unsafe_allow_html=True)

elif slide == 5:
    st.markdown('<div class="section-title">🚀 Live Demo: Book Your Slot</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        location = st.selectbox("Location", ["Sydney CBD", "Parramatta", "Chatswood", "Homebush"], key="loc")
        date = st.date_input("Date", datetime.today(), key="date")
    with col2:
        time = st.time_input("Time", datetime.now().time(), key="time")
        plate = st.text_input("Car Plate", max_chars=10, placeholder="e.g. ABC123", key="plate")

    if st.button("📥 Book Slot"):
        if plate:
            st.success(f"✅ Booked {plate} at {location} on {date} {time.strftime('%I:%M %p')}")
            if "bookings" not in st.session_state:
                st.session_state.bookings = []
            st.session_state.bookings.append({
                "Location": location,
                "Date": date,
                "Time": time.strftime("%I:%M %p"),
                "Plate": plate
            })
        else:
            st.warning("Please enter car plate.")

elif slide == 6:
    st.markdown('<div class="section-title">📋 Booking History</div>', unsafe_allow_html=True)
    if "bookings" in st.session_state and st.session_state.bookings:
        df = pd.DataFrame(st.session_state.bookings)
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No bookings yet.")

elif slide == 7:
    st.markdown('<div class="title">🎉 Thank You!</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Any Questions? Ready for Viva!</div>', unsafe_allow_html=True)

# --- Navigation Buttons ---
cols = st.columns([1, 4, 1])
with cols[0]:
    if slide > 1:
        st.button("⬅️ Back", on_click=prev_slide)
with cols[2]:
    if slide < 7:
        st.button("Next ➡️", on_click=next_slide)

