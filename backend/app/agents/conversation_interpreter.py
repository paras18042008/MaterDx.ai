import json

from app.llm.ollama_client import chat
from app.reasoning.reasoning_context import ReasoningContext


SYSTEM_PROMPT = """
You are the Clinical Language Interpreter for MaterDx.

Your ONLY job is to convert patient language into structured medical evidence.

RULES:
- Never diagnose
- Never assess risk
- Never suggest treatment
- Never suggest tests
- Never ask questions

OUTPUT MUST BE VALID JSON ONLY.

SCHEMA:

{
  "new_evidence": [
    {
      "type": "symptom",
      "name": "",
      "severity": "",
      "duration": "",
      "onset": "",
      "location": "",
      "radiation": "",
      "confidence": 0.0
    }
  ],
  "negated_evidence": [],
  "uncertain_evidence": [],
  "confidence": 0.0
}

If no evidence is found, return empty lists.

Return ONLY JSON.
"""


class ConversationInterpreter:

    def __init__(self):
        self.model = "llama3"

    def build_prompt(self, context: ReasoningContext):

        return f"""
Previous Question:
{context.last_question}

Conversation History:
{context.conversation_history}

Patient Message:
{context.current_message}

Return valid JSON only.
"""

    def interpret(self, context: ReasoningContext):

        prompt = self.build_prompt(context)

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
            return json.loads(text)

        except Exception:

            return {
                "new_evidence": [],
                "negated_evidence": [],
                "uncertain_evidence": [],
                "confidence": 0.0,
                "error": "invalid_json",
                "raw_response": text,
            }