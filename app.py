import streamlit as st

st.title("AI Student Companion")

user_input = st.text_input("Ask me anything")

if user_input:
    user_input = user_input.lower()

    if "study" in user_input or "timetable" in user_input or "plan" in user_input:
        st.write("📅 Here’s a simple study timetable:")
        st.write("""
Morning:
- 2 hrs coding
- 1 hr revision

Afternoon:
- 2 hrs core subjects
- Practice questions

Evening:
- 1 hr revision
- 1 hr light study

Night:
- Quick revision + plan next day
        """)

    elif "exam" in user_input:
        st.write("📝 Exam Tips:")
        st.write("- Revise important topics")
        st.write("- Practice PYQs")
        st.write("- Stay confident")

    elif "motivate" in user_input:
        st.write("🔥 Keep going Aman! You’ll achieve 9.5+ CGPA 💯")

    else:
        st.write("Try asking about study plan, timetable, exam or motivation.")
