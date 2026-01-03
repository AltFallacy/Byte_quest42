import random

MEMORY_WORD_SETS = [
    ["Apple", "Table", "Penny"],
    ["River", "Chair", "Bread"],
    ["Dog", "Bottle", "Paper"],
    ["Tree", "Phone", "Coin"],
    ["Book", "Glass", "Orange"]
]

ATTENTION_WORDS = [
    "WORLD", "TRAIN", "PLANT", "HOUSE", "MONEY"
]

ARITHMETIC_QUESTIONS = [
    (100, 7),
    (93, 6),
    (80, 9),
    (72, 8),
    (65, 5)
]

LOGIC_QUESTIONS = [
    ("Is 10:10 a valid time on an analog clock?", "Yes"),
    ("Does a week have 7 days?", "Yes"),
    ("Is February always 28 days?", "No"),
    ("Can a triangle have four sides?", "No"),
    ("Is midnight AM?", "Yes")
]

def get_daily_questions(seed=None):
    if seed is not None:
        random.seed(seed)

    return {
        "memory_words": random.choice(MEMORY_WORD_SETS),
        "attention_word": random.choice(ATTENTION_WORDS),
        "arithmetic": random.choice(ARITHMETIC_QUESTIONS),
        "logic": random.choice(LOGIC_QUESTIONS)
    }
