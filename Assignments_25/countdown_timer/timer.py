import streamlit as st
import time

st.title("⏳ Countdown Timer")

if 'running' not in st.session_state:
    st.session_state.running = False

if not st.session_state.running:
    minutes = st.number_input("Enter minutes:", min_value=0, max_value=60, value=0)
    seconds = st.number_input("Enter seconds:", min_value=0, max_value=60, value=0)
    total_seconds = int(minutes * 60 + seconds)
    st.session_state.total_seconds = total_seconds

if st.button("Start Timer"):
    st.session_state.running = True

if st.session_state.running and st.session_state.total_seconds > 0:
    mins, secs = divmod(st.session_state.total_seconds, 60)
    timer_display = f"{mins:02d}:{secs:02d}"
    st.write(f"Time Left: {timer_display}")
    st.session_state.total_seconds -= 1
    time.sleep(1)
    st.rerun()

if st.session_state.running and st.session_state.total_seconds == 0:
    st.success("⏰ Time's up!")
    st.session_state.running = False
