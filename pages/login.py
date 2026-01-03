import streamlit as st

st.title("🔐 Login")

username = st.text_input("Enter your username")

if st.button("Login"):
    if username:
        st.session_state["user"] = username
        st.success(f"Logged in as {username}")
    else:
        st.warning("Please enter a username")
