import json

from app.llm.ollama_client import chat


SYSTEM_PROMPT = """
You are the Doctor Agent of MaterDx (MD*A).

You are an experienced physician.

Your ONLY responsibility is to analyze the Patient Context and produce your current differential diagnosis.

Do NOT worry about criticism.
Do NOT debate.
Do NOT ask multiple questions.

Produce your BEST clinical opinion.

Return ONLY valid JSON.

SCHEMA

{
    "hypotheses":[
        {
            "name":"",
            "confidence":0.0,
            "supporting_evidence":[],
            "missing_information":[]
        }
    ],

    "risk":"",

    "next_question":"",

    "reasoning":""
}
"""


class DoctorAgent:

    def __init__(self):

        self.model = "llama3"

    def build_prompt(
        self,
        patient_context,
    ):

        return f"""
PATIENT CONTEXT

{patient_context}

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

            patient_context.doctor_output = json.loads(text)

        except Exception:

            patient_context.doctor_output = {
                "hypotheses": [],
                "risk": "UNKNOWN",
                "next_question": "",
                "reasoning": "",
                "error": "invalid_json",
                "raw_response": text,
            }

        return patient_context