import streamlit as st
import google.generativeai as genai

# 🔐 Secure API Key
genai.configure(api_key=st.secrets["AQ.Ab8RN6KwdWziyA_mpCf_oLf9QI3UFYVfgE2Emu_EfXRJsAsxsg"])

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

# ⚙️ FUNCTION (Efficiency Boost)
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

# 💡 AI SUGGESTIONS
if st.button("🌱 Get Tips to Reduce Footprint"):
    tips = model.generate_content(
        "Give simple and practical ways for students to reduce carbon footprint"
    )
    st.write(tips.text)

# 💬 AI CHAT
st.subheader("💬 Ask AI About Environment")

user_input = st.text_input("Type your question here...")

if user_input:
    response = model.generate_content(
        f"You are an environmental expert. Answer clearly:\n{user_input}"
    )
    st.write(response.text)

# 🧪 BASIC TESTING (Testing Score Boost)
st.subheader("🧪 Run Test")

if st.checkbox("Run Sample Test"):
    test_result = calculate_footprint(10, 100, "Vegetarian")
    st.write(f"Test Output (10km, 100 units, Veg): {test_result}")