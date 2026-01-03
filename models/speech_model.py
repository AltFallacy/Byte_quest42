from utils.nlp_utils import lexical_diversity, avg_sentence_length

def speech_drift_score(text: str) -> float:
    if len(text.strip()) == 0:
        return 0.0

    lex_div = lexical_diversity(text)
    sent_len = avg_sentence_length(text)

    # Simple heuristic drift score
    score = 1.0 - (0.6 * lex_div + 0.4 * min(sent_len / 20, 1))
    return round(score, 3)
