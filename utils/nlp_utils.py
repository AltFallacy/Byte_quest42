import re

def lexical_diversity(text: str) -> float:
    words = re.findall(r'\w+', text.lower())
    if not words:
        return 0.0
    return len(set(words)) / len(words)

def avg_sentence_length(text: str) -> float:
    sentences = re.split(r'[.!?]', text)
    sentences = [s for s in sentences if s.strip()]
    if not sentences:
        return 0.0
    return sum(len(s.split()) for s in sentences) / len(sentences)
