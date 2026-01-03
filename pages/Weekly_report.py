import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

from models.cognitive_model import cognitive_anomaly_score
from models.speech_model import speech_drift_score
from models.behavior_model import behavior_score
from models.fusion_model import fusion_score

# --------------------------------------------------
# Page Setup
# --------------------------------------------------
st.title("📊 Weekly Cognitive Report")
st.markdown("AI-generated summary based on **longitudinal trends**, not a single test.")

# --------------------------------------------------
# Auth Check
# --------------------------------------------------
if "user" not in st.session_state or not st.session_state["user"]:
    st.warning("Please login first.")
    st.stop()

user = st.session_state["user"]
DATA_PATH = "data/user_sessions.csv"

# --------------------------------------------------
# Load Data
# --------------------------------------------------
try:
    df = pd.read_csv(DATA_PATH)
except FileNotFoundError:
    st.info("No assessment data found yet.")
    st.stop()

user_df = df[df["user"] == user].copy()

if len(user_df) < 5:
    st.info("Complete at least **5 daily check-ins** to unlock your weekly report.")
    st.stop()

# Convert date column
user_df["date"] = pd.to_datetime(user_df["date"])
user_df.sort_values("date", inplace=True)

st.subheader("📅 Data Summary")
st.write(f"Total sessions: **{len(user_df)}**")
st.write(f"Date range: **{user_df['date'].iloc[0].date()} → {user_df['date'].iloc[-1].date()}**")

# --------------------------------------------------
# 1️⃣ Cognitive Trend Analysis
# --------------------------------------------------
st.subheader("🧠 Cognitive Trend")

avg_score = user_df["normalized_score"].mean()
trend = user_df["normalized_score"].iloc[-1] - user_df["normalized_score"].iloc[0]

reaction_time_proxy = (1 - user_df["normalized_score"]) * 1000 + 400
reaction_time_mean = reaction_time_proxy.mean()

cognitive_features = np.array([
    [reaction_time_mean, avg_score * 100]
])

cog_score = cognitive_anomaly_score(cognitive_features)

st.line_chart(user_df.set_index("date")["normalized_score"])

# --------------------------------------------------
# 2️⃣ Speech & Language Drift
# --------------------------------------------------
st.subheader("🗣 Speech & Language Trends")

speech_sessions = user_df[user_df["speech_used"] == 1]

if len(speech_sessions) >= 2:
    speech_lengths = speech_sessions["transcript_length"].values
    speech_trend = speech_lengths[-1] - speech_lengths[0]
    speech_score = speech_drift_score(speech_lengths.reshape(-1, 1))
    st.write(f"Speech entries analyzed: **{len(speech_sessions)}**")
else:
    speech_score = 0.0
    st.info("Not enough speech samples for trend analysis.")

# --------------------------------------------------
# 3️⃣ Behavioral Drift
# --------------------------------------------------
st.subheader("📉 Behavioral Patterns")

behavior_features = user_df[["missed_tasks", "delay_minutes"]].values
beh_score = behavior_score(behavior_features)

st.line_chart(
    user_df.set_index("date")[["missed_tasks", "delay_minutes"]]
)

# --------------------------------------------------
# 4️⃣ Fusion Model (FINAL OUTPUT)
# --------------------------------------------------
st.divider()
st.header("🧾 Weekly Cognitive Stability Report")

final_score, explanation = fusion_score(
    cog_score,
    speech_score,
    beh_score
)

st.metric("Overall Cognitive Stability Score", round(final_score, 2))

st.subheader("🔍 Explainability")
for e in explanation:
    st.write(f"- {e}")

# --------------------------------------------------
# Interpretation (Non-Diagnostic)
# --------------------------------------------------
if final_score >= 0.75:
    st.success("✅ Cognitive patterns appear stable over this period.")
elif 0.5 <= final_score < 0.75:
    st.warning("⚠️ Mild cognitive or behavioral drift observed.")
else:
    st.error("❗ Significant deviation from baseline patterns detected.")

st.info(
    """
This report is based on **trend analysis over time**.
It does **not** diagnose any medical condition.
Consider professional evaluation if concerns persist.
"""
)
