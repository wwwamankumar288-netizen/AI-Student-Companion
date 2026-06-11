import streamlit as st
import google.generativeai as genai
import os

# 🔐 Secure API Key (Works for both Streamlit Cloud & Local)
api_key = st.secrets.get("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("❌ API key not found. Please set GEMINI_API_KEY in Streamlit secrets.")
    st.stop()

genai.configure(api_key=api_key)

# 🤖 AI Model
model = genai.GenerativeModel("gemini-pro")

# 🌍 App Title
st.title("🌍 Carbon Footprint Awareness AI")

st.markdown("""
### 🌱 About This App
This platform helps users calculate their carbon footprint based on daily activities 
and provides AI-powered suggestions to reduce environmental impact.
""")

st.caption("Enter your daily habits to estimate your environmental impact.")

# 📊 INPUT SECTION
st.subheader("📊 Enter Your Daily Data")

distance = st.number_input(
    "🚗 Daily Travel (km)",
    min_value=0.0,
    help="Enter how many kilometers you travel daily"
)

electricity = st.number_input(
    "⚡ Monthly Electricity Usage (units)",
    min_value=0.0,
    help="Enter your monthly electricity consumption"
)

diet = st.selectbox(
    "🍽️ Your Diet Type",
    ["Vegetarian", "Non-Vegetarian", "Vegan"]
)

# ⚙️ FUNCTION
def calculate_footprint(distance, electricity, diet):
    footprint = (distance * 0.21) + (electricity * 0.5)

    if diet == "Non-Vegetarian":
        footprint += 2
    elif diet == "Vegetarian":
        footprint += 1
    else:
        footprint += 0.5

    return footprint

# 📈 RESULT SECTION
st.subheader("📈 Results")

result = None  # store result globally

if st.button("🌿 Calculate Carbon Footprint"):
    if distance == 0 and electricity == 0:
        st.warning("⚠️ Please enter some data to calculate footprint")
    else:
        result = calculate_footprint(distance, electricity, diet)

        st.success(f"🌍 Your Estimated Carbon Footprint: {result:.2f} kg CO2/day")

        if result < 5:
            st.info("✅ Great! Your carbon footprint is low.")
        elif result < 10:
            st.warning("⚠️ Moderate footprint. Try reducing it.")
        else:
            st.error("❌ High footprint! Take action now.")

# 💡 AI SUGGESTIONS (Personalized)
if st.button("🌱 Get Tips to Reduce Footprint"):
    if distance == 0 and electricity == 0:
        st.warning("⚠️ Please calculate your footprint first")
    else:
        result = calculate_footprint(distance, electricity, diet)

        with st.spinner("Generating AI tips..."):
            tips = model.generate_content(
                f"""
                User Details:
                - Daily Travel: {distance} km
                - Electricity: {electricity} units/month
                - Diet: {diet}
                - Estimated Footprint: {result:.2f} kg CO2/day

                Give simple, practical, student-friendly ways to reduce this footprint.
                """
            )
        st.write(tips.text)

# 💬 AI CHAT
st.subheader("💬 Ask AI About Environment")

user_input = st.text_input("Type your question here...")

if user_input:
    with st.spinner("Thinking..."):
        response = model.generate_content(
            f"You are an environmental expert. Answer clearly and simply:\n{user_input}"
        )
    st.write(response.text)

# 🧪 BASIC TESTING
st.subheader("🧪 Run Test")

if st.checkbox("Run Sample Test"):
    test_result = calculate_footprint(10, 100, "Vegetarian")
    st.write(f"Test Output (10km, 100 units, Veg): {test_result}")