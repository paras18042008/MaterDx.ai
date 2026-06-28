QUESTION_TREE = {
    "cardiac": {
        "LOW": [
            "Do you feel mild chest discomfort?",
            "Does it come and go?"
        ],
        "MEDIUM": [
            "Is the pain triggered by exertion?",
            "Do you feel breathless during pain?"
        ],
        "HIGH": [
            "Is the pain radiating to left arm or jaw?",
            "Do you have sweating or nausea?",
            "Is the pain constant for more than 1 hour?"
        ],
        "EMERGENCY": [
            "Call emergency services immediately.",
            "Are you alone right now?"
        ]
    },

    "respiratory": {
        "LOW": [
            "Do you have mild cough?",
        ],
        "HIGH": [
            "Are you struggling to breathe?",
            "Any chest tightness or wheezing?"
        ]
    },

    "general": {
        "LOW": [
            "Any fever or fatigue?"
        ]
    }
}


def get_next_questions(category, risk):
    return QUESTION_TREE.get(category, {}).get(risk, [
        "Can you describe your symptoms more?"
    ])