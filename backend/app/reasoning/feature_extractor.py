import json
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"


def safe_parse(text):
    """
    Safely parse JSON returned by the LLM.
    If parsing fails, return an empty schema.
    """

    try:
        return json.loads(text)

    except Exception:
        return {
            "chief_complaint": None,
            "symptoms": [],
            "negatives": [],
            "red_flags": [],
            "attributes": {}
        }


def extract_features(patient_message: str):
    """
    Extract structured medical findings from free-text.
    This module NEVER diagnoses.
    It ONLY extracts facts.
    """

    prompt = f"""
You are an expert clinical information extraction engine.

Your ONLY task is to convert a patient's message into structured JSON.

DO NOT diagnose.

DO NOT estimate probability.

DO NOT explain.

DO NOT add information that the patient never mentioned.

Return ONLY valid JSON.

Schema:

{{
    "chief_complaint": "",

    "symptoms": [
        {{
            "name": "",
            "severity": "",
            "duration": "",
            "location": "",
            "radiation": "",
            "onset": ""
        }}
    ],

    "negatives": [],

    "red_flags": [],

    "attributes": {{
        "age_related": "",
        "pregnancy": "",
        "trauma": ""
    }}
}}

Patient:

\"\"\"{patient_message}\"\"\"

Return ONLY JSON.
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }
    )

    raw = response.json()["response"]

    return safe_parse(raw)