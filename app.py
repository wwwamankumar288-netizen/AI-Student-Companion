import streamlit as st
import google.generativeai as genai
from functools import lru_cache

---------------- CONFIG ----------------

st.set_page_config(page_title="Carbon Footprint AI", layout="centered")

---------------- TITLE ----------------

st.title("🌍 Carbon Footprint Awareness AI")
st.markdown("Calculate your footprint and get smart suggestions to reduce it.")

---------------- API KEY ----------------

api_key = st.text_input("🔐 Enter your Gemini API Key", type="password")

if not api_key:
st.warning("Please enter your API key to continue")
st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-pro")

---------------- INPUT SECTION ----------------

st.header("📊 Enter Your Daily Data")

distance = st.number_input(
"🚗 Daily Travel (km)",
min_value=0.0,
help="Enter how many kilometers you travel daily"
)

electricity = st.number_input(
"⚡ Monthly Electricity Usage (units)",
min_value=0.0,
help="Enter monthly electricity usage in units (kWh)"
)

diet = st.selectbox(
"🍽️ Your Diet Type",
["Vegetarian", "Non-Vegetarian", "Vegan"],
help="Diet impacts carbon emissions"
)

---------------- CORE LOGIC ----------------

@lru_cache(maxsize=100)
def calculate_footprint(distance, electricity, diet):
footprint = (distance * 0.21) + (electricity * 0.5)

if diet == "Non-Vegetarian":
    footprint += 2
elif diet == "Vegetarian":
    footprint += 1
else:
    footprint += 0.5

return round(footprint, 2)

---------------- CALCULATION ----------------

if st.button("🌿 Calculate Carbon Footprint"):
if distance == 0 and electricity == 0:
st.warning("⚠️ Please enter valid data")
else:
result = calculate_footprint(distance, electricity, diet)

    st.success(f"🌍 Your Estimated Footprint: {result} kg CO₂/day")

    if result < 5:
        st.info("✅ Great! Your carbon footprint is low.")
    elif result < 10:
        st.warning("⚠️ Moderate footprint. Consider reducing usage.")
    else:
        st.error("🚨 High footprint! Take action immediately.")

---------------- AI TIPS ----------------

if st.button("🌱 Get Smart Tips"):
result = calculate_footprint(distance, electricity, diet)

with st.spinner("Generating AI suggestions..."):
    try:
        prompt = f"""
        A student has:
        - Travel: {distance} km/day
        - Electricity: {electricity} units/month
        - Diet: {diet}
        - Carbon Footprint: {result} kg CO2/day

        Give practical, simple and low-cost ways to reduce footprint.
        """

        tips = model.generate_content(prompt)
        st.subheader("💡 Personalized Tips")
        st.write(tips.text)

    except Exception as e:
        st.error("Error generating tips. Check API key or try again.")

---------------- CHAT ----------------

st.header("💬 Ask AI About Environment")

user_input = st.text_input(
"Ask any environmental question",
placeholder="e.g., How can I reduce carbon footprint in college?"
)

if user_input:
try:
response = model.generate_content(user_input)
st.write(response.text)
except:
st.error("Failed to get response. Try again.")

---------------- FOOTER ----------------

st.markdown("---")
st.caption("Built for Carbon Awareness 🌱 | Optimized with caching & validation")