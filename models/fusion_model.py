def fusion_score(cog, speech, behavior):
    weights = {
        "cognitive": 0.4,
        "speech": 0.35,
        "behavior": 0.25
    }

    final = (
        cog * weights["cognitive"] +
        speech * weights["speech"] +
        behavior * weights["behavior"]
    )

    explanation = []
    if cog > 0.3:
        explanation.append("↑ Reaction time or accuracy deviation detected")
    if speech > 0.3:
        explanation.append("↓ Language complexity trend observed")
    if behavior > 0.3:
        explanation.append("↑ Behavioral inconsistency detected")

    if not explanation:
        explanation.append("No significant cognitive drift detected")

    return round(final, 3), explanation
