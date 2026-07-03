import json

from app.llm.ollama_client import chat


SYSTEM_PROMPT = """
You are the Conversation Interpreter Agent for MaterDx (MD.v1).

You are NOT a doctor.

Your ONLY responsibility is to convert the patient's latest response into structured clinical information.

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
- The patient's latest response MUST ALWAYS be interpreted together with the Previous Question.
- Many responses such as "Yes", "No", "Sometimes", "Since yesterday", "Only while walking", or "Not anymore" are incomplete on their own. Use the Previous Question to determine exactly what clinical information those responses refer to.
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

        self.model = "llama3"

    def build_prompt(
        self,
        patient_context,
        patient_message,
    ):

        return f"""
PATIENT CONTEXT

{patient_context}

------------------------------------

PREVIOUS QUESTION ASKED TO THE PATIENT

{patient_context.last_question}

------------------------------------

LATEST PATIENT RESPONSE

{patient_message}

------------------------------------

Interpret the patient's response in the context of the Previous Question.

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