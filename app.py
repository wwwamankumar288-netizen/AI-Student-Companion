import streamlit as st
import google.generativeai as genai

# 🔐 Secure API Key (IMPORTANT)
genai.configure(api_key=st.secrets["API_KEY"])

# 🎯 AI Model
model = genai.GenerativeModel("gemini-pro")

# 🌍 App Title
st.title("🌍 Carbon Footprint Awareness AI")
st.markdown("Track, understand and reduce your carbon footprint using AI 🤖")

# 📊 USER INPUT SECTION
st.subheader("📊 Enter Your Daily Data")

distance = st.number_input("🚗 Daily Travel (in km)", min_value=0.0)
electricity = st.number_input("⚡ Monthly Electricity Usage (units)", min_value=0.0)
diet = st.selectbox("🍽️ Your Diet Type", ["Vegetarian", "Non-Vegetarian", "Vegan"])

# 🧮 CALCULATE FOOTPRINT
if st.button("🌿 Calculate Carbon Footprint"):
    footprint = (distance * 0.21) + (electricity * 0.5)

    if diet == "Non-Vegetarian":
        footprint += 2
    elif diet == "Vegetarian":
        footprint += 1
    else:
        footprint += 0.5

    st.success(f"🌍 Your Estimated Carbon Footprint: {footprint:.2f} kg CO2/day")

# 💡 AI SUGGESTIONS
if st.button("🌱 Get Tips to Reduce Footprint"):
    tips = model.generate_content(
        "Give simple and practical ways for students to reduce carbon footprint"
    )
    st.write(tips.text)

# 🤖 AI CHAT SECTION
st.subheader("💬 Ask AI Anything About Environment")

user_input = st.text_input("Type your question here...")

if user_input:
    response = model.generate_content(
        f"You are an environmental expert. Answer clearly:\n{user_input}"
    )
    st.write(response.text)
