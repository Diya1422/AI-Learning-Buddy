import streamlit as st
import google.generativeai as genai

from prompts import (
    explain_prompt,
    example_prompt,
    quiz_prompt,
    feedback_prompt,
    session_prompt
)

# ---------------- Load CSS ----------------
def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---------------- Gemini Configuration ----------------
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("GOOGLE_API_KEY not found. Please create a .env file.")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="AI Learning Buddy",
    page_icon="🎓",
    layout="centered"
)

load_css()

# ---------------- Session State ----------------
if "history" not in st.session_state:
    st.session_state.history = []

if "topic" not in st.session_state:
    st.session_state.topic = ""

# ---------------- Sidebar ----------------
st.sidebar.title("🎓 AI Learning Buddy")

st.sidebar.info("""
### About

**Created By:** Diya Sharma

**Topic:** Machine Learning Fundamentals
""")

theme = st.sidebar.selectbox(
    "🎨 Theme",
    ["Light", "Dark"]
)

if theme == "Dark":
    st.markdown("""
    <style>
    .stApp{
        background:#1E1E1E;
        color:white;
    }
    </style>
    """, unsafe_allow_html=True)

if st.sidebar.button("🗑 Clear Chat"):
    st.session_state.history = []
    st.rerun()

# ---------------- Title ----------------
st.title("🎓 AI Learning Buddy")

st.subheader("Learn Machine Learning in a Simple Way")

st.markdown("""
<div style="
background:white;
padding:20px;
border-radius:15px;
box-shadow:0px 2px 10px rgba(0,0,0,0.1);
">

### 👋 Welcome!

Learn Machine Learning concepts through:

- 📘 Explanations
- 🌍 Real-Life Examples
- 📝 Quiz Generation
- 💬 Feedback
- 🎯 Complete Learning Sessions

</div>
""", unsafe_allow_html=True)

# ---------------- Progress ----------------
st.markdown("### 📊 Learning Progress")

progress = min(len(st.session_state.history) * 10, 100)

st.progress(progress)

st.write(f"Progress : {progress}%")

# ---------------- Suggested Topics ----------------
st.markdown("### 💡 Suggested Topics")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🤖 Supervised Learning"):
        st.session_state.topic = "Supervised Learning"

with col2:
    if st.button("🌳 Decision Tree"):
        st.session_state.topic = "Decision Tree"

with col3:
    if st.button("🧠 Neural Network"):
        st.session_state.topic = "Neural Network"

# ---------------- User Input ----------------
topic = st.text_input(
    "📚 Enter Topic",
    value=st.session_state.topic,
    placeholder="Example: Supervised Learning"
)

activity = st.selectbox(
    "🎯 Choose Activity",
    [
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz",
        "Check My Answer",
        "Complete Learning Session",
        "Ask Anything"
    ]
)

generate = st.button("🚀 Generate")

st.divider()

# ---------------- AI Response ----------------
if generate:

    if topic.strip() == "":
        st.warning("Please enter a topic.")

    else:

        if activity == "Explain Concept":
            prompt = explain_prompt(topic)

        elif activity == "Real-Life Example":
            prompt = example_prompt(topic)

        elif activity == "Generate Quiz":
            prompt = quiz_prompt(topic)

        elif activity == "Check My Answer":
            prompt = feedback_prompt(topic)

        elif activity == "Complete Learning Session":
            prompt = session_prompt(topic)

        else:
            prompt = topic

        try:

            with st.spinner("🤖 AI is thinking..."):
                response = model.generate_content(prompt)

            st.success("Response Generated Successfully!")

            st.markdown("## 📖 AI Response")

            st.info(response.text)

            words = len(response.text.split())
            characters = len(response.text)

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Words", words)

            with col2:
                st.metric("Characters", characters)

            st.download_button(
                "📥 Download Response",
                response.text,
                file_name="AI_Response.txt",
                mime="text/plain"
            )

            st.session_state.history.append({
                "topic": topic,
                "activity": activity,
                "response": response.text
            })

        except Exception as e:
            st.error(e)

# ---------------- Chat History ----------------
if st.session_state.history:

    st.markdown("---")

    st.header("💬 Chat History")

    for chat in reversed(st.session_state.history):

        st.markdown(f"### 📚 {chat['topic']}")

        st.write(f"**Activity :** {chat['activity']}")

        st.success(chat["response"])

        st.divider()

# ---------------- Footer ----------------
st.markdown("---")

st.caption("🎓 AI Learning Buddy | Built using Streamlit + Google Gemini")