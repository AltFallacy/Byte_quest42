import numpy as np
from sklearn.ensemble import IsolationForest

# Dummy pretrained model for hackathon
model = IsolationForest(contamination=0.1, random_state=42)

# Fit with synthetic baseline
baseline = np.array([
    [500, 90],
    [550, 88],
    [520, 92],
    [530, 89]
])
model.fit(baseline)

def cognitive_anomaly_score(features: np.ndarray) -> float:
    score = model.decision_function(features)
    return float(-score[0])  # higher = worse
