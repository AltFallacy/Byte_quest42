from utils.nlp_utils import lexical_diversity, avg_sentence_length

def speech_drift_score(text: str) -> float:
    """
    Computes a heuristic speech drift score based on linguistic simplicity.
    Output range: 0.0 (stable) → 1.0 (higher drift risk)
    """

    text = text.strip()

    # Guard: very short or empty speech is not reliable
    if len(text.split()) < 5:
        return 0.0

    lex_div = lexical_diversity(text)          # 0–1
    sent_len = avg_sentence_length(text)       # words per sentence

    # Normalize sentence length (cap at 25 words)
    sent_len_norm = min(sent_len / 25.0, 1.0)

    # Penalize overly simplistic language
    complexity_score = (0.6 * lex_div) + (0.4 * sent_len_norm)

    # Drift is inverse of linguistic complexity
    drift_score = 1.0 - complexity_score

    # Bound safety
    drift_score = max(0.0, min(drift_score, 1.0))

    return round(drift_score, 3)
