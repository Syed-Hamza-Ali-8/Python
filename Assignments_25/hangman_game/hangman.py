import streamlit as st
import random

st.title("😄 Hangman Game")

words = [
    "python", "variable", "function", "loop", "string", "integer", "boolean", 
    "compiler", "list", "tuple", "set", "syntax", "dictionary", "streamlit" , 
    "binary", "class", "object", "inheritance", "method", "module", "package"
]

if 'selected_word' not in st.session_state:
    st.session_state.selected_word = random.choice(words)

if 'guessed_letters' not in st.session_state:
    st.session_state.guessed_letters = []
if 'attempts_left' not in st.session_state:
    st.session_state.attempts_left = 6

selected_word = st.session_state.selected_word

display_word = ""
for letter in selected_word:
    if letter in st.session_state.guessed_letters:
        display_word += letter + " "
    else:
        display_word += "_ "

st.write(f"Word: {display_word.strip()}")
st.write(f"Attempts Left: {st.session_state.attempts_left}")
st.write(f"Guessed Letters: {' '.join(st.session_state.guessed_letters)}")

guess = st.text_input("Guess a letter (a-z):", key="guess_input")

if st.button("Submit Guess"):
    if guess.isalpha() and len(guess) == 1:
        if guess in st.session_state.guessed_letters:
            st.warning("You already guessed that letter!")
        else:
            st.session_state.guessed_letters.append(guess)
            if guess not in selected_word:
                st.session_state.attempts_left -= 1
        st.rerun()
    else:
        st.error("Please enter a single valid letter (a-z)!")

if all(letter in st.session_state.guessed_letters for letter in selected_word):
    st.success(f"🎉 You WON! The word was '{selected_word}'.")
    if st.button("Play Again"):
        st.session_state.clear()
        st.rerun()

elif st.session_state.attempts_left == 0:
    st.error(f"💀 Game Over! The word was '{selected_word}'.")
    if st.button("Try Again"):
        st.session_state.clear()
        st.rerun()
