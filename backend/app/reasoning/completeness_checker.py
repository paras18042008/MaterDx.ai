def get_missing_features(extracted: dict):
    """
    Determines what clinical information is still missing.
    This is deterministic logic (NO LLM here).
    """

    # Base checklist for chest pain (v1 rule set)
    required = {
        "duration",
        "severity",
        "location",
        "radiation",
        "onset",
        "shortness_of_breath",
        "sweating",
        "nausea"
    }

    present = set()

    # ----------------------------
    # Extract known fields
    # ----------------------------
    if extracted.get("symptoms"):
        for symptom in extracted["symptoms"]:
            if symptom.get("duration"):
                present.add("duration")
            if symptom.get("severity"):
                present.add("severity")
            if symptom.get("location"):
                present.add("location")
            if symptom.get("radiation"):
                present.add("radiation")
            if symptom.get("onset"):
                present.add("onset")

    # ----------------------------
    # Handle red flags / symptoms
    # ----------------------------
    text_blob = str(extracted)

    if "shortness_of_breath" in text_blob or "breathless" in text_blob:
        present.add("shortness_of_breath")

    if "sweating" in text_blob or "diaphoresis" in text_blob:
        present.add("sweating")

    if "nausea" in text_blob:
        present.add("nausea")

    # ----------------------------
    # Compute missing
    # ----------------------------
    missing = list(required - present)

    return missing