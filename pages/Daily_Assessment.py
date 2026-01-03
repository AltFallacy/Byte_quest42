import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import os

from utils.audio_utils import transcribe_audio
from utils.question_bank import get_daily_questions

# --------------------------------------------------
# Page Setup
# --------------------------------------------------
st.title("🧠 Daily Cognitive Check-in")
st.markdown("⏱ Takes ~3 minutes. Used for weekly trend analysis.")

# --------------------------------------------------
# Auth Check
# --------------------------------------------------
if "user" not in st.session_state or not st.session_state["user"]:
    st.warning("Please login first.")
    st.stop()

user = st.session_state["user"]
today = datetime.now().date()

# --------------------------------------------------
# Data Setup
# --------------------------------------------------
DATA_DIR = "data"
DATA_PATH = os.path.join(DATA_DIR, "user_sessions.csv")
os.makedirs(DATA_DIR, exist_ok=True)

# --------------------------------------------------
# Prevent Multiple Submissions per Day
# --------------------------------------------------
if os.path.exists(DATA_PATH):
    df_existing = pd.read_csv(DATA_PATH)
    if ((df_existing["user"] == user) & (df_existing["date"] == str(today))).any():
        st.success("✅ Today's assessment already submitted.")
        st.stop()

# --------------------------------------------------
# Stable Daily Randomness
# --------------------------------------------------
seed = hash(f"{user}_{today}")
questions = get_daily_questions(seed)

# --------------------------------------------------
# 1️⃣ Cognitive Screening
# --------------------------------------------------
st.header("1️⃣ Cognitive Screening")

score = 0
max_score = 10

# Orientation
year = st.text_input("What is the current year?")
if year == str(datetime.now().year):
    score += 1

place = st.text_input("Where are you right now?")
if place.strip():
    score += 1

# Memory
st.subheader("🧠 Memory")
words = questions["memory_words"]
st.info("Remember these words:")
st.success(", ".join(words))

recall = st.text_input("Type the words you remember (space separated):").lower()
if recall:
    recalled = recall.split()
    score += sum(w.lower() in recalled for w in words)

# Attention
st.subheader("🎯 Attention")
att_word = questions["attention_word"]
backward = st.text_input(f"Spell '{att_word}' backwards:")
if backward.lower() == att_word.lower()[::-1]:
    score += 1

# Arithmetic
st.subheader("➗ Calculation")
base, sub = questions["arithmetic"]
calc = st.number_input(f"What is {base} − {sub} ?", step=1)
if calc == base - sub:
    score += 1

# Language
st.subheader("🗣 Language")
sentence = st.text_input("Write a meaningful sentence:")
if len(sentence.split()) >= 3:
    score += 1

# Logical Reasoning
st.subheader("🕒 Logical Reasoning")
logic_q, logic_ans = questions["logic"]
choice = st.radio(logic_q, ["Yes", "No"])
if choice == logic_ans:
    score += 1

# --------------------------------------------------
# 2️⃣ Speech & Language Journal (IN-APP)
# --------------------------------------------------
st.header("2️⃣ Speech & Language Journal")
st.markdown("🎙 Speak for **30–60 seconds** about your day.")

audio_data = st.audio_input("Record your voice")

speech_used = 0
transcript = ""

if audio_data is not None:
    try:
        with st.spinner("Transcribing audio..."):
            transcript = transcribe_audio(audio_data)
            speech_used = 1

        st.subheader("📝 Transcription Preview")
        st.write(transcript)

    except Exception:
        st.warning("Speech processing unavailable today.")
        transcript = ""
        speech_used = 0

# --------------------------------------------------
# 3️⃣ Behavioral Self-Report
# --------------------------------------------------
st.header("3️⃣ Daily Behavior")

missed_tasks = st.slider("Missed planned tasks today", 0, 10, 0)
delay = st.slider("Average response delay today (minutes)", 0, 120, 10)

# --------------------------------------------------
# 4️⃣ Save Daily Session
# --------------------------------------------------
st.divider()

if st.button("💾 Save Today's Assessment"):
    row = {
        "user": user,
        "date": today,
        "cognitive_score": score,
        "max_score": max_score,
        "normalized_score": score / max_score,
        "missed_tasks": missed_tasks,
        "delay_minutes": delay,
        "speech_used": speech_used,
        "transcript_length": len(transcript.split()),
        "question_seed": seed
    }

    df_new = pd.DataFrame([row])

    if os.path.exists(DATA_PATH):
        df_new.to_csv(DATA_PATH, mode="a", header=False, index=False)
    else:
        df_new.to_csv(DATA_PATH, index=False)

    st.success("✅ Assessment saved! Come back tomorrow.")
