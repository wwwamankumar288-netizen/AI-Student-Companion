import streamlit as st

# ---------------- CONFIG ----------------
st.set_page_config(page_title="AI Student Companion", page_icon="🤖")

# ---------------- TITLE ----------------
st.title("🎓 AI Student Companion")
st.write("Your smart study buddy 🚀")

# ---------------- INPUT ----------------
user_input = st.text_input("Ask me anything:")

# ---------------- LOGIC ----------------
def get_response(query):
    query = query.lower()

    if "hello" in query:
        return "Hey there! 👋"
    elif "study" in query:
        return "📚 Try Pomodoro: 25 min study + 5 min break"
    elif "motivation" in query:
        return "🔥 Keep going! You're closer than you think."
    elif "code" in query:
        return "💻 Practice daily on LeetCode / GFG!"
    else:
        return "🤖 I’m still learning! Ask something else."

# ---------------- OUTPUT ----------------
if user_input:
    response = get_response(user_input)
    st.write("### 🤖 Answer:")
    st.success(response)