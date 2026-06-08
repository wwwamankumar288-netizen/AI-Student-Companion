import streamlit as st

st.title("🎓 AI Student Companion")

user_input = st.text_input("Ask me anything:")

def generate_response(query):
    query = query.lower()

    if "study plan" in query:
        return "📚 Study daily + revise + practice"
    elif "time table" in query:
        return "🕒 Morning study, afternoon practice, evening revision"
    elif "motivation" in query:
        return "🔥 Stay consistent!"
    else:
        return "🤖 Ask about study plans or exams!"

if user_input:
    st.write(generate_response(user_input))
