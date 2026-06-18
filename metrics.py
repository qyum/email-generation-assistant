def fact_recall_score(email, facts):


    email_lower = email.lower()

    matched = 0

    for fact in facts:

        words = fact.lower().split()

        if any(word in email_lower for word in words):
            matched += 1

    return round(matched / len(facts), 2)


def tone_accuracy_score(email, tone):

    email_lower = email.lower()

    tone_keywords = {
    "formal": [
        "dear",
        "regards",
        "sincerely"
    ],

    "warm": [
        "thank you",
        "pleasure",
        "appreciate"
    ],

    "professional": [
        "regards",
        "thank you"
    ],

    "empathetic": [
        "understand",
        "sorry",
        "appreciate"
    ],

    "friendly": [
        "thank you",
        "happy",
        "great"
    ],

    "respectful": [
        "thank you",
        "respect",
        "appreciate"
    ],

    "enthusiastic": [
        "excited",
        "looking forward",
        "great"
    ],

    "polite": [
        "please",
        "thank you",
        "kindly"
    ]
}

    keywords = tone_keywords.get(tone.lower(), [])

    if len(keywords) == 0:
        return 0.5

    matches = 0

    for word in keywords:
        if word in email_lower:
            matches += 1

    return round(matches / len(keywords), 2)


def format_adherence_score(email):

    email_lower = email.lower()

    score = 0

    if "subject:" in email_lower:
        score += 1

    if "dear" in email_lower:
        score += 1

    if (
        "best regards" in email_lower
        or "regards" in email_lower
        or "sincerely" in email_lower
    ):
        score += 1

    return round(score / 3, 2)
