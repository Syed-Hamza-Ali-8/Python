import streamlit as st
import random
import string

COMMON_PASSWORDS = {"password", "12345678", "qwerty", "password123", "helloworld", "admin123"}

def check_password_strength(password):
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    if any(c.islower() for c in password) and any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Include both uppercase and lowercase letters.")
    
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Include at least one number (0-9).")

    if any(c in "!@#$%^&*" for c in password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&*).")

    if password.lower() in COMMON_PASSWORDS:
        feedback.append("This password is too common! Choose a more unique one.")
    else:
        score += 1  # Ensure full 5/5 score when all conditions are met

    strength = "Weak" if score <= 2 else "Moderate" if score < 5 else "Strong"
    return score, strength, feedback

def generate_strong_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(characters) for _ in range(12))

st.title("🔐 Password Strength Meter")
password = st.text_input("Enter a password :", type="password")

if st.button("Check Strength"):
    if password:
        score, strength, feedback = check_password_strength(password)
        st.subheader(f"Strength: {strength} ({score}/5)")

        if strength == "Weak":
            st.warning("Your password is weak! Consider these improvements:")
            for tip in feedback:
                st.write(f"- {tip}")
        elif strength == "Moderate":
            st.info("Your password is decent, but could be stronger!")
        else:
            st.success("Great! Your password is strong. ✅")
    else:
        st.error("Please enter a password to check.")

if st.button("Suggest a Strong Password"):
    strong_password = generate_strong_password()
    st.text(f"Suggested Password: {strong_password}")
