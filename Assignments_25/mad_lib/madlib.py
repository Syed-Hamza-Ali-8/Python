import streamlit as st
import random

st.title("🏏 Cricket Mad Lib Generator")

st.write("Fill in the blanks with your words to create a funny cricket story!")

batsman = st.text_input("Enter your favorite batsman's name")
bowler = st.text_input("Enter a famous bowler's name")
team = st.text_input("Enter a cricket team name")
run = st.number_input("Enter a number (for runs)", min_value=1, max_value=500, step=1)
adjective = st.text_input("Enter an adjective (e.g., fast, hilarious)")
stadium = st.text_input("Enter a stadium name")

if st.button("Generate Cricket Story"):
    templates = [
        f"In a thrilling match at {stadium}, {batsman} smashed {run} runs against {team}. The crowd went wild as {bowler} tried to bowl a {adjective} delivery but failed miserably!",
        f"{batsman} walked onto the pitch at {stadium} with confidence. Facing {bowler}'s {adjective} bowling, they hit every ball for a boundary, making {team} fans cheer loudly!",
        f"It was a sunny day at {stadium}. {team} was struggling until {batsman} arrived. Facing {bowler}'s {adjective} bouncers, {batsman} scored {run} runs, leading the team to victory!"
    ]
    
    story = random.choice(templates)
    st.subheader("🏆 Your Cricket Story:")
    st.write(story)
