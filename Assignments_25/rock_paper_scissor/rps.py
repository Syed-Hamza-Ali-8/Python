import streamlit as st
import random

st.title("✊✋✌️ Rock, Paper, Scissors Game")

st.write("Choose your move and try to beat the computer!")

# Options
options = ["Rock", "Paper", "Scissors"]

user_choice = st.selectbox("Your Move:", options)

if st.button("Play"):
    computer_choice = random.choice(options)
    
    st.write(f"🤖 Computer chose: **{computer_choice}**")
    st.write(f"🧑 You chose: **{user_choice}**")

    if user_choice == computer_choice:
        st.info("It's a **Tie!** 😐")
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        st.success("🎉 **You Win!**")
    else:
        st.error("💀 **Computer Wins!**")
        
    st.write("---")
    st.write("Play again by selecting a move!")

