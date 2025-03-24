import streamlit as st

st.set_page_config(page_title="Guess the Number (Computer)", page_icon="🤖")
st.title("🤖 Computer Guesses Your Number!")

st.write("Think of a number between **1 and 100**, and I will keep guessing until I find it! You give me hints manually.")

if "low" not in st.session_state:
    st.session_state.low = 1
    st.session_state.high = 100
    st.session_state.attempts = 0
    st.session_state.guess = None
    st.session_state.game_over = False

def reset_game():
    st.session_state.low = 1
    st.session_state.high = 100
    st.session_state.attempts = 0
    st.session_state.guess = None
    st.session_state.game_over = False

st.button("🔄 Restart Game", on_click=reset_game)

if not st.session_state.game_over:
    if st.session_state.low > st.session_state.high:
        st.error("⚠️ You've given conflicting hints! No valid numbers left. Please restart the game.")
    else:
        if st.session_state.guess is None:
            st.session_state.guess = (st.session_state.low + st.session_state.high) // 2
            st.session_state.attempts += 1

        st.subheader(f"My Guess: **{st.session_state.guess}**")

        col1, col2, col3 = st.columns(3)

        if col1.button("🔻 Too Low"):
            st.session_state.low = st.session_state.guess + 1
            if st.session_state.low > st.session_state.high:
                st.error("❌ No numbers left! You might've misclicked.")
            else:
                st.session_state.guess = (st.session_state.low + st.session_state.high) // 2
                st.session_state.attempts += 1

        if col2.button("🎯 Correct!"):
            st.success(f"Yay! I guessed your number **{st.session_state.guess}** in {st.session_state.attempts} attempts! 🎉")
            st.balloons()
            st.session_state.game_over = True

        if col3.button("🔺 Too High"):
            st.session_state.high = st.session_state.guess - 1
            if st.session_state.low > st.session_state.high:
                st.error("I couldn't have guessed your number")
            else:
                st.session_state.guess = (st.session_state.low + st.session_state.high) // 2
                st.session_state.attempts += 1

if st.session_state.game_over:
    st.info("Press 'Restart Game' to play again!")
