from app.reasoning.clinical_state import ClinicalState
from app.reasoning.question_planner import get_next_question

state = ClinicalState()

state.risk = "HIGH"
state.systems["cardiac"] = 80
state.missing_features = ["sweating", "nausea"]

print(get_next_question(state))