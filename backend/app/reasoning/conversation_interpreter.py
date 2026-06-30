from app.llm.ollama_client import chat


SYSTEM_PROMPT = """
You are the Conversation Interpreter for MaterDx.

Your ONLY job is to understand the patient's latest reply in the context of the previous question.

Return ONLY valid JSON.

Never explain.

Never use markdown.

Output format:

{
    "answered_question":"",
    "answer_type":"",
    "value":"",
    "confidence":0.0,
    "needs_clarification":false,
    "clarification_reason":""
}

Rules:

- answer_type can ONLY be:
    yes
    no
    value
    uncertain
    unrelated

- confidence must be between 0 and 1.

- If the reply clearly answers the previous question,
confidence should be high.

- If unsure, return needs_clarification=true.

Return JSON only.
"""


def interpret_reply(previous_question, user_reply):
    prompt = f"""
Previous Question:
{previous_question}

Patient Reply:
{user_reply}
"""

    response = chat(
        model="llama3",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
    )

    return response["message"]["content"]