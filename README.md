# 🧠 SilentMind
### AI-Powered Cognitive Drift Detection Using Digital Biomarkers

---

## 1. Problem Statement

Silent neurological diseases such as dementia progress gradually and often remain undetected until symptoms become severe. Traditional diagnostic methods are infrequent, clinical, and reactive, making early intervention difficult. There is a need for a non-invasive, continuous, and accessible system that can monitor early cognitive and behavioral changes over time.

---

## 2. Project Name

**SilentMind**

---

## 3. Team Name

**Orion **  


---

## 4. Deployed Link (Optional)

🔗 https://your-deployed-link-here  
*(If not deployed, mention: Not Deployed)*

---

## 5. 2-Minute Demonstration Video Link

🎥

---

## 6. PPT Link

📊 

---

# 📘 Standard README

## 🧩 Project Overview

SilentMind is an AI-powered cognitive health monitoring application that detects **longitudinal cognitive and behavioral drift** using digital biomarkers.  
The system does **not diagnose dementia or any medical condition**, but instead highlights patterns and deviations from a user’s personal baseline that may indicate early cognitive risk.

The project leverages **multimodal AI** combining cognitive tests, speech analysis, text analysis, and behavioral consistency to generate explainable insights.

> ⚠️ Disclaimer: SilentMind is a screening and monitoring tool, not a medical diagnostic system.

---

## ⚙️ Setup and Installation Instructions

### Prerequisites
- Python 3.9+
- pip / virtualenv
- Microphone access (for voice input)



silentmind/
│
├── app.py                      # Streamlit entry point
├── requirements.txt
│
├── models/
│   ├── cognitive_model.py      # Model 1
│   ├── speech_model.py         # Model 2
│   ├── behavior_model.py       # Model 3
│   └── fusion_model.py         # Model 4
│
├── utils/
│   ├── audio_utils.py
│   └── nlp_utils.py
│
└── data/
    └── demo_user.csv           # optional demo storage


### Installation Steps

```bash
git clone https://github.com/your-repo/silentmind.git
cd silentmind
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt




