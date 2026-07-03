import json

from app.llm.ollama_client import chat


SYSTEM_PROMPT = """
You are the Critic Agent of MaterDx (MD*A).

You are a senior physician reviewing another doctor's work.

You receive:

1. The complete Patient Context.
2. The Doctor Agent's opinion.

Your job is NOT to make an independent diagnosis from scratch.

Your responsibilities:

- Find weaknesses in the doctor's reasoning.
- Find overlooked diagnoses.
- Find contradictions.
- Find unsupported assumptions.
- Suggest a better next question if appropriate.
- NEVER simply agree unless the reasoning is already strong.

Return ONLY valid JSON.

SCHEMA

{
    "agreement": true,

    "criticisms": [],

    "additional_hypotheses":[
        {
            "name":"",
            "confidence":0.0
        }
    ],

    "recommended_changes":[],

    "suggested_next_question":"",

    "reasoning":""
}
"""


class CriticAgent:

    def __init__(self):

        self.model = "llama3"

    def build_prompt(
        self,
        patient_context,
    ):

        return f"""
PATIENT CONTEXT

{patient_context}

------------------------------------

DOCTOR OPINION

{patient_context.doctor_output}

------------------------------------

Review the doctor's opinion.

Return ONLY valid JSON.
"""

    def run(
        self,
        patient_context,
    ):

        prompt = self.build_prompt(
            patient_context,
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

            patient_context.critic_output = json.loads(text)

        except Exception:

            patient_context.critic_output = {
                "agreement": False,
                "criticisms": [],
                "additional_hypotheses": [],
                "recommended_changes": [],
                "suggested_next_question": "",
                "reasoning": "",
                "error": "invalid_json",
                "raw_response": text,
            }

        return patient_context