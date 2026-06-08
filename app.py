import streamlit as st
import google.generativeai as genai   # 👈 AI import

# 👉 API setup (TOP)
genai.configure(api_key="YOUR_API_KEY_HERE")

# 👉 UI (TOP)
st.title("🎓 AI Student Companion")
st.markdown("Your smart study assistant 🤖")

# 👉 BUTTONS
st.subheader("Choose an option 👇")

if st.button("📅 Study Timetable"):
    st.write("Here’s your study timetable...")

if st.button("📝 Exam Tips"):
    st.write("Revise, practice PYQs, stay calm!")

if st.button("🔥 Motivation"):
    st.write("You got this Aman! 💯")

# 👉 AI MODEL (MIDDLE)
model = genai.GenerativeModel("gemini-pro")

# 👉 USER INPUT (LAST)
user_input = st.text_input("Ask anything:")

if user_input:
    response = model.generate_content(user_input)
    st.write(response.text)
