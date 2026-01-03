import numpy as np

def behavior_score(features: np.ndarray) -> float:
    missed_tasks, delay = features[0]

    score = 0.0
    score += missed_tasks * 0.15
    score += min(delay / 60, 1) * 0.5

    return round(score, 3)
