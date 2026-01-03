import streamlit as st
import numpy as np
from utils.audio_utils import transcribe_audio
from models.cognitive_model import cognitive_anomaly_score
from models.speech_model import speech_drift_score
from models.behavior_model import behavior_score
from models.fusion_model import fusion_score

# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(page_title="SilentMind", layout="centered")

st.title("🧠 SilentMind")
st.subheader("AI‑Powered Cognitive Drift Detection")
st.markdown("⚠️ **Educational screening only. Not a medical diagnosis.**")

# --------------------------------------------------
# 1️⃣ Cognitive Screening Test
# --------------------------------------------------
st.header("1️⃣ Cognitive Screening Test")

score = 0
max_score = 10

# Orientation
year = st.text_input("What is the current year?")
place = st.text_input("Where are you right now? (home / college / hospital etc.)")

if year == "2026":
    score += 1
if place.strip():
    score += 1

# Memory
st.subheader("🧠 Memory Test")
words = ["Apple", "Table", "Penny"]
st.success(", ".join(words))

recall = st.text_input("Type the words you remember (space separated):").lower()
if recall:
    recalled = recall.split()
    for w in ["apple", "table", "penny"]:
        if w in recalled:
            score += 1

# Attention
st.subheader("🎯 Attention")
backward = st.text_input("Spell the word 'WORLD' backwards:")
if backward.lower() == "dlrow":
    score += 1

# Calculation
st.subheader("➗ Calculation")
calc = st.number_input("What is 100 − 7 ?", step=1)
if calc == 93:
    score += 1

# Language
st.subheader("🗣 Language")
sentence = st.text_input("Type a meaningful sentence:")
if len(sentence.split()) >= 3:
    score += 1

# Logical Reasoning
st.subheader("🕒 Logical Reasoning")
clock = st.radio("Is 10:10 a valid time on an analog clock?", ["Yes", "No"])
if clock == "Yes":
    score += 1

# --------------------------------------------------
# 2️⃣ Optional Speech Input
# --------------------------------------------------
st.header("2️⃣ Speech & Language Analysis")

audio_file = st.file_uploader(
    "Upload a short voice note (30–60 seconds)",
    type=["wav", "mp3", "m4a"]
)

speech_score = 0.0
transcript = ""

if audio_file is not None:
    with st.spinner("Transcribing audio..."):
        transcript = transcribe_audio(audio_file.read())

    st.subheader("📝 Transcribed Text")
    st.write(transcript)

    speech_score = speech_drift_score(transcript)

# --------------------------------------------------
# 3️⃣ Behavioral Input
# --------------------------------------------------
st.header("3️⃣ Behavioral Patterns")

missed_tasks = st.slider("Missed Tasks (last 7 days)", 0, 10, 1)
delay = st.slider("Average Response Delay (minutes)", 0, 120, 10)

behavior_features = np.array([[missed_tasks, delay]])
beh_score = behavior_score(behavior_features)

# --------------------------------------------------
# 4️⃣ AI Fusion Output
# --------------------------------------------------
st.divider()

if st.button("📊 Generate Cognitive Report"):
    # Convert screening score → ML‑friendly proxy
    normalized_score = score / max_score
    reaction_time_proxy = (1 - normalized_score) * 1000 + 400

    cognitive_features = np.array([
        [reaction_time_proxy, normalized_score * 100]
    ])

    cog_score = cognitive_anomaly_score(cognitive_features)

    final_score, explanation = fusion_score(
        cog_score, speech_score, beh_score
    )

    st.subheader("🧾 Screening Result")
    st.write(f"**Cognitive Test Score:** {score} / {max_score}")
    st.metric("Overall Cognitive Stability Score", round(final_score, 2))

    st.write("### 🔍 Explainability")
    for e in explanation:
        st.write(f"- {e}")

    if score >= 8:
        st.success("✅ Cognitive function appears stable")
    elif 5 <= score < 8:
        st.warning("⚠️ Mild cognitive drift detected")
    else:
        st.error("❗ Significant cognitive drift detected")

    st.info("This tool supports early awareness and does not replace professional evaluation.")

