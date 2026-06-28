from app.reasoning.feature_extractor import extract_features
from app.reasoning.clinical_state import clinical_state
from app.reasoning.clinical_updater import update_state

state = clinical_state()

features = extract_features(
    "I've had severe chest pain radiating to my left arm for two hours."
)

state = update_state(state, features)

print(state.to_dict())