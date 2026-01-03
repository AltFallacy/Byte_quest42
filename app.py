import streamlit as st

# --------------------------------------------------
# App Config
# --------------------------------------------------
st.set_page_config(
    page_title="SilentMind",
    page_icon="🧠",
    layout="centered"
)

# --------------------------------------------------
# Session State Init
# --------------------------------------------------
if "user" not in st.session_state:
    st.session_state["user"] = None

# --------------------------------------------------
# Sidebar Navigation
# --------------------------------------------------
st.sidebar.title("🧠 SilentMind")

if st.session_state["user"]:
    st.sidebar.success(f"Logged in as: {st.session_state['user']}")
else:
    st.sidebar.info("Not logged in")

st.sidebar.markdown("---")
st.sidebar.markdown("📌 **Navigation**")
st.sidebar.markdown(
    """
    - 🏠 Home  
    - 🔐 Login  
    - 🧠 Daily Assessment  
    - 📊 Weekly Report  
    """
)

st.sidebar.markdown("---")
st.sidebar.caption("Educational screening only · Not a medical diagnosis")

# --------------------------------------------------
# Landing Content
# --------------------------------------------------
st.title("🧠 SilentMind")
st.subheader("AI-Powered Cognitive Drift Detection")

st.markdown(
    """
SilentMind helps track **cognitive stability over time** using short,
non-invasive daily interactions.

### How it works
1. Login with a username  
2. Complete short **daily cognitive check-ins**  
3. Data is stored locally and securely  
4. AI analyzes **trends over time**  
5. A **weekly explainable report** is generated  

⚠️ **This tool does not diagnose dementia or any medical condition.**
"""
)

st.info("👈 Use the sidebar to navigate through the app")


