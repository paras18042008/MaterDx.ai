import json

from app.llm.ollama_client import chat


SYSTEM_PROMPT = """
You are the Conversation Interpreter Agent for MaterDx (MD*A).

You are NOT a doctor.

Your ONLY responsibility is to convert the patient's latest message into structured clinical information.

IMPORTANT PRINCIPLES

- Extract EVERY clinically relevant fact.
- Never diagnose.
- Never estimate disease probability.
- Never assess risk.
- Never recommend treatment.
- Never recommend investigations.
- Never ask questions.
- Never invent information.
- Never hallucinate.
- Preserve uncertainty instead of guessing.
- Extract ONLY NEW information relative to the supplied Patient Context.
- If information already exists in Patient Context, do not repeat it.
- Return ONLY valid JSON.

SCHEMA

{
    "new_information": {

        "demographics": {},

        "chief_complaint": {},

        "symptoms": [],

        "signs": [],

        "vitals": [],

        "medications": [],

        "allergies": [],

        "past_medical_history": [],

        "surgical_history": [],

        "family_history": [],

        "social_history": [],

        "occupational_history": [],

        "travel_history": [],

        "lifestyle": [],

        "menstrual_history": {},

        "pregnancy_history": {},

        "immunizations": [],

        "devices": [],

        "lab_results": [],

        "imaging": [],

        "procedures": [],

        "risk_factors": [],

        "red_flags": [],

        "negated_findings": [],

        "uncertain_findings": [],

        "timeline": []

    },

    "confidence": 0.0,

    "missing_information": [],

    "ambiguities": []
}

Every symptom should preserve as much structure as possible.

Example:

{
    "name": "Chest pain",
    "severity": "Severe",
    "onset": "Sudden",
    "duration": "3 hours",
    "frequency": "Constant",
    "location": "Central chest",
    "radiation": "Left arm",
    "quality": "Pressure",
    "progression": "Worsening",
    "aggravating_factors": [],
    "relieving_factors": [],
    "associated_features": [],
    "confidence": 0.98
}

Return ONLY JSON.
"""


class ConversationInterpreter:

    def __init__(self):

        self.model = "qwen3"

    def build_prompt(
        self,
        patient_context,
        patient_message,
    ):

        return f"""
PATIENT CONTEXT

{patient_context}

------------------------------------

LATEST PATIENT MESSAGE

{patient_message}

------------------------------------

Extract ONLY NEW clinically relevant information.

Return ONLY valid JSON.
"""

    def run(
        self,
        patient_context,
        patient_message,
    ):

        prompt = self.build_prompt(
            patient_context,
            patient_message,
        )

        response = chat(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
        )

        text = response["message"]["content"]

        try:

            patient_context.interpreter_output = json.loads(text)

        except Exception:

            patient_context.interpreter_output = {

                "new_information": {},

                "confidence": 0.0,

                "missing_information": [],

                "ambiguities": [],

                "error": "invalid_json",

                "raw_response": text,
            }

        return patient_context