def fusion_score(cog, speech, behavior):
    """
    Combines multimodal drift scores into a single cognitive stability index.
    Inputs expected in range [0.0, 1.0]
    Output:
      final_score (0.0 = stable, 1.0 = high drift)
      explanation (list of human-readable reasons)
    """

    # -----------------------------
    # Base weights (prior belief)
    # -----------------------------
    base_weights = {
        "cognitive": 0.4,
        "speech": 0.35,
        "behavior": 0.25
    }

    signals = {
        "cognitive": cog,
        "speech": speech,
        "behavior": behavior
    }

    # -----------------------------
    # Handle missing / weak signals
    # -----------------------------
    active_signals = {k: v for k, v in signals.items() if v is not None}

    if not active_signals:
        return 0.0, ["Insufficient data for risk assessment"]

    # Renormalize weights based on available signals
    weight_sum = sum(base_weights[k] for k in active_signals)
    weights = {k: base_weights[k] / weight_sum for k in active_signals}

    # -----------------------------
    # Compute final risk score
    # -----------------------------
    final_score = sum(active_signals[k] * weights[k] for k in active_signals)
    final_score = max(0.0, min(final_score, 1.0))

    # -----------------------------
    # Explainability (contribution-aware)
    # -----------------------------
    explanation = []

    for signal, value in active_signals.items():
        contribution = value * weights[signal]

        if value >= 0.6:
            level = "high"
        elif value >= 0.3:
            level = "moderate"
        else:
            level = "low"

        if signal == "cognitive" and value >= 0.3:
            explanation.append(
                f"Cognitive performance shows {level} deviation from baseline"
            )

        if signal == "speech" and value >= 0.3:
            explanation.append(
                f"Speech and language patterns show {level} simplification"
            )

        if signal == "behavior" and value >= 0.3:
            explanation.append(
                f"Daily behavior consistency shows {level} variability"
            )

    if not explanation:
        explanation.append("Cognitive and behavioral patterns appear stable")

    return round(final_score, 3), explanation
