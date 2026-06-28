import requests
import json
import re

OLLAMA_URL = "http://localhost:11434/api/generate"


# -----------------------------
# SAFE JSON PARSER (ROBUST)
# -----------------------------
def safe_parse(text):
    """
    Extracts JSON from LLM output safely.
    Works even if model adds extra explanation text.
    """

    try:
        # Try to find JSON block inside response
        match = re.search(r"\{.*\}", text, re.DOTALL)

        if match:
            return json.loads(match.group())

    except Exception as e:
        print("JSON parse error:", e)
        print("Raw model output:", text)

    # fallback (NEVER block system)
    return {
        "category": "general",
        "risk": "MEDIUM",
        "flags": []
    }


# -----------------------------
# MAIN CLASSIFIER FUNCTION
# -----------------------------
def classify_symptom(state):
    prompt = f"""
You are a STRICT medical triage classification engine.

You are NOT a doctor.
You do NOT diagnose diseases.

You ONLY classify symptoms into structured JSON.

-----------------------
RULES (VERY IMPORTANT):
-----------------------
1. Output ONLY valid JSON
2. NO explanations
3. NO markdown
4. NO extra text before or after JSON
5. If unsure, choose "general" and "MEDIUM"

-----------------------
ALLOWED VALUES:
-----------------------

category:
- cardiac
- respiratory
- neurological
- gastrointestinal
- musculoskeletal
- general

risk:
- LOW
- MEDIUM
- HIGH
- EMERGENCY

flags:
- list of observed symptoms (strings only)

-----------------------
OUTPUT FORMAT (STRICT):
-----------------------
{{
  "category": "cardiac",
  "risk": "HIGH",
  "flags": ["chest_pain", "radiation"]
}}

-----------------------
PATIENT INPUT:
-----------------------
{json.dumps(state, indent=2)}
"""

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            },
            timeout=30
        )

        data = response.json()
        raw_output = data.get("response", "")

        return safe_parse(raw_output)

    except Exception as e:
        print("Ollama request failed:", e)

        return {
            "category": "general",
            "risk": "MEDIUM",
            "flags": []
        }