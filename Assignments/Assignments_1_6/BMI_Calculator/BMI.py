import streamlit as st

def calculate_bmi(weight, height_m):
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)

def convert_to_meters(feet, inches):
    total_inches = feet * 12 + inches
    meters = total_inches * 0.0254
    return meters

st.title("BMI Calculator")

st.write("Enter your details:")

weight = st.number_input("Enter your weight (kg):", min_value=1.0, max_value=500.0, step=0.5)

feet = st.number_input("Feet:", min_value=1, max_value=8, step=1)
inches = st.number_input("Inches:", min_value=0, max_value=11, step=1)

if st.button("Calculate BMI"):
    height_m = convert_to_meters(feet, inches)

    if weight and height_m > 0:
        bmi = calculate_bmi(weight, height_m)
        st.success(f"Your BMI is: {bmi}")

        if bmi < 18.5:
            st.info("You are underweight")
        elif 18.5 <= bmi < 24.9:
            st.success("You have a normal weight")
        elif 25 <= bmi < 29.9:
            st.warning("You are overweight")
        else:
            st.error("You are obese.")
    else:
        st.error("Please enter valid values.")
