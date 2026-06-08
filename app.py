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
        - 1 hr light study / notes

        Night:
        - Quick revision + plan next day
        """)

    elif "exam" in user_input:
        st.write("📝 Exam Tips:")
        st.write("- Revise important topics")
        st.write("- Practice previous papers")
        st.write("- Stay calm and confident")

    elif "motivate" in user_input:
        st.write("🔥 You got this Aman! Stay consistent, success will follow.")

    else:
        st.write("Try asking about study plan, timetable, motivation, or exam tips.")
