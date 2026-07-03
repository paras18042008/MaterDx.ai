import json

from app.llm.ollama_client import chat


SYSTEM_PROMPT = """
You are the Judge Agent of MaterDx (MD*A).

You are the FINAL clinical decision maker.

You receive:

1. The complete Patient Context.
2. The Doctor Agent's opinion.
3. The Critic Agent's review.

Your responsibilities:

- Decide the current differential diagnosis.
- Decide the current clinical risk.
- Decide the single best next question.
- Decide whether enough information has been collected to generate a report.

You do NOT have to agree with either the Doctor or the Critic.

Your job is to make the BEST possible clinical decision using all available evidence.

Return ONLY valid JSON.

SCHEMA

{
    "risk":"",

    "hypotheses":[
        {
            "name":"",
            "confidence":0.0
        }
    ],

    "next_question":"",

    "ready_for_report":false,

    "reasoning":""
}
"""


class JudgeAgent:

    def __init__(self):

        self.model = "qwen3:8b"

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

CRITIC REVIEW

{patient_context.critic_output}

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

            patient_context.judge_output = json.loads(text)

        except Exception:

            patient_context.judge_output = {
                "risk": "UNKNOWN",
                "hypotheses": [],
                "next_question": "",
                "ready_for_report": False,
                "reasoning": "",
                "error": "invalid_json",
                "raw_response": text,
            }

        return patient_context