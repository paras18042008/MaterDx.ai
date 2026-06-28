from app.reasoning.clinical_state import ClinicalState
from app.reasoning.completeness_checker import get_missing_features

def update_state(state: ClinicalState, extracted):

    # ----------------------------
    # Chief complaint
    # ----------------------------
    if extracted.get("chief_complaint"):
        state.confirmed_features.append(
            extracted["chief_complaint"]
        )

    # ----------------------------
    # Symptoms
    # ----------------------------
    for symptom in extracted.get("symptoms", []):

        name = symptom.get("name", "")

        if name and name not in state.confirmed_features:
            state.confirmed_features.append(name)

        # ----------------------------
        # Simple reasoning (Version 1)
        # ----------------------------

        if name.lower() == "chest pain":

            state.systems["cardiac"] += 60
            state.systems["respiratory"] += 15
            state.systems["gastrointestinal"] += 10
            state.systems["musculoskeletal"] += 15

            
        radiation = symptom.get("radiation", "")

        if radiation:

            state.confirmed_features.append(
                f"radiation:{radiation}"
            )

            state.systems["cardiac"] += 20

    # ----------------------------
    # Risk
    # ----------------------------

    if state.systems["cardiac"] >= 80:
        state.risk = "HIGH"

    elif state.systems["cardiac"] >= 50:
        state.risk = "MEDIUM"

    else:
        state.risk = "LOW"

    state.missing_features = get_missing_features(extracted)

    return state