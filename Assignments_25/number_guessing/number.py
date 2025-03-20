import streamlit as st
import random

st.title("🎯 Guess the Number Game")

st.write("I'm thinking of a number between 1 and 100. Can you guess it?")

if 'number' not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0

guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

if st.button("Submit Guess"):
    st.session_state.attempts += 1
    if guess < st.session_state.number:
        st.write("🔻 Too low! Try a higher number.")
    elif guess > st.session_state.number:
        st.write("🔺 Too high! Try a lower number.")
    else:
        st.success(f"🎉 Congratulations! You guessed the number {st.session_state.number} in {st.session_state.attempts} attempts!")
        st.session_state.number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.balloons()
