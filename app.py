import random
import streamlit as st

st.set_page_config(page_title="Ask Jeebs", page_icon="🐾", layout="centered")

st.markdown("""
<style>
.stApp {
    background-color: #111111;
    color: white;
}
h1, h2, h3, p, label, div {
    color: white !important;
}
.stTextInput input {
    background-color: #222222;
    color: white;
}
.stButton button {
    background-color: #333333;
    color: white;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# Rimage header 
st.image("jeebs_header.png", use_container_width=True)

st.title("Ask Jeebs")

responses = [
    "Well that’s actually pretty tricky because I’m small. But you could try googling it.",
    "That’s too easy, you could figure it out.",
    "My parents told me I’m not supposed to talk about that.",
    "It sounds like you could solve this by knocking something off the counter. Maybe try that first.",
    "I considered your question carefully and then forgot it immediately.",
    "That feels like a dog problem.",
    "Have you tried yelling at a closed door?",
    "I’m going to need approximately 14 naps before I can answer that.",
    "The answer is probably in the treat cabinet.",
    "I don’t know, but I support your journey emotionally from over here.",
    "That question has big vacuum cleaner energy, and I don’t like it.",
    "Maybe stare at the wall for 20 minutes and see if anything changes.",
]

if "answered" not in st.session_state:
    st.session_state.answered = False
if "response" not in st.session_state:
    st.session_state.response = ""

question = st.text_input("Okay, what even the heck do you want to know?")

if st.button("Ask Jeebs"):
    if question.strip():
        st.session_state.response = random.choice(responses)
        st.session_state.answered = True
    else:
        st.warning("Jeebs requires at least one tiny crumb of a question.")

if st.session_state.answered:
    st.subheader(st.session_state.response)

    st.write("Did Jeebs resolve your question?")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Yes"):
            st.success("Okay so do you want to give me a pinch?")

    with col2:
        if st.button("No"):
            st.error("What even the frik!")
            st.session_state.answered = False
            st.session_state.response = ""
            st.rerun()
