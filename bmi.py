import streamlit as st

# 🎯 Page Title
st.title("💪 Body Mass Index Calculator")

# 📏 User Inputs
height = st.slider("Enter your height (in cm):", 100, 250, 175)
weight = st.slider("Enter your weight (in kg):", 40, 200, 70)

# 📊 Calculate BMI
bmi = weight / ((height / 100) ** 2)

# 📌 Display BMI Result
st.write(f"📊 **Your BMI is:** {bmi:.2f}")

# 🏆 BMI Categories
st.markdown("### **BMI Categories:**")
st.write("🔵 **Underweight:** BMI less than 18.5")
st.write("🟢 **Normal Weight:** BMI between 18.5 and 24.9")
st.write("🟠 **Overweight:** BMI between 25 and 29.9")
st.write("🔴 **Obesity:** BMI 30 or more")


st.markdown("Created By Asad Jilani GIAIC (7534) Email : a.jee1975@gmail.com")


