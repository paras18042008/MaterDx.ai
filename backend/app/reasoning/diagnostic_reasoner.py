import json

from app.llm.ollama_client import chat


SYSTEM_PROMPT = """
You are MaterDx's Diagnostic Reasoner.

You receive structured medical evidence.

Your job is to:

1. Generate a ranked differential diagnosis.
2. Assign confidence (0-1).
3. List supporting evidence.
4. List contradicting evidence.
5. List missing evidence.
6. Estimate overall patient risk:
   LOW
   MODERATE
   HIGH
   EMERGENCY
7. Decide the single best next question.

Return ONLY valid JSON.

Output format:

{
  "risk": "",
  "hypotheses": [],
  "next_question": "",
  "ready_for_report": false
}

Never explain.
Never use markdown.
Return JSON only.
"""


class DiagnosticReasoner:

    def reason(self, evidence):

        prompt = f"""
Evidence:

{json.dumps(evidence, indent=2)}
"""

        response = chat(
            model="llama3",
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

        return json.loads(response["message"]["content"])