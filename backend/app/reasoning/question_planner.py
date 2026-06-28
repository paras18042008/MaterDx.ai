def get_next_question(state):
    """
    Decides the next best clinical question.
    This is rule-based v1 (no LLM yet).
    """

    missing = state.missing_features
    systems = state.systems
    risk = state.risk

    # ----------------------------
    # HIGH RISK PRIORITY PATH
    # ----------------------------
    if risk == "HIGH":

        if "shortness_of_breath" in missing:
            return "Are you experiencing shortness of breath?"

        if "sweating" in missing:
            return "Are you sweating or feeling clammy?"

        if "nausea" in missing:
            return "Do you feel nausea or vomiting?"

        if "duration" in missing:
            return "How long has the pain been present?"

    # ----------------------------
    # CARDIAC PRIORITY PATH
    # ----------------------------
    if systems["cardiac"] >= 50:

        if "radiation" in missing:
            return "Does the pain radiate to your arm, jaw, or back?"

        if "severity" in missing:
            return "How severe is your pain on a scale of 1 to 10?"

        if "location" in missing:
            return "Where exactly is the pain located?"

    # ----------------------------
    # DEFAULT PATH
    # ----------------------------
    if missing:
        return f"Can you tell me more about your {missing[0]}?"

    return "Can you describe your symptoms in more detail?"