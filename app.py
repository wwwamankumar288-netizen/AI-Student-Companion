import streamlit as st
import google.generativeai as genai

# 🔐 Ask user for API key (safe + easy)
api_key = st.text_input("Enter your Gemini API Key", type="password")

if not api_key:
    st.warning("Please enter your API key to continue")
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

# 📊 INPUT SECTION
st.subheader("📊 Enter Your Daily Data")

distance = st.number_input("🚗 Daily Travel (km)", min_value=0.0)
electricity = st.number_input("⚡ Monthly Electricity Usage (units)", min_value=0.0)

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

# 📈 CALCULATE
if st.button("🌿 Calculate Carbon Footprint"):
    if distance == 0 and electricity == 0:
        st.warning("Enter some data first")
    else:
        result = calculate_footprint(distance, electricity, diet)
        st.success(f"🌍 Footprint: {result:.2f} kg CO2/day")

# 💡 AI TIPS
if st.button("🌱 Get Tips"):
    result = calculate_footprint(distance, electricity, diet)

    with st.spinner("Generating tips..."):
        tips = model.generate_content(
            f"""
            Travel: {distance} km
            Electricity: {electricity}
            Diet: {diet}
            Footprint: {result:.2f}

            Give simple ways to reduce carbon footprint for a student.
            """
        )
    st.write(tips.text)

# 💬 CHAT
st.subheader("💬 Ask AI")

user_input = st.text_input("Ask anything about environment")

if user_input:
    response = model.generate_content(user_input)
    st.write(response.text)