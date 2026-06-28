import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"


def safe_parse(text):
    try:
        return json.loads(text)
    except:
        return {
            "urgency": "MEDIUM",
            "suggestion": "Unable to parse AI response",
            "possible_conditions": []
        }


def analyze_patient(data):
    prompt = f"""
You are a medical triage AI system.

Return ONLY valid JSON.

Format:
{{
  "urgency": "LOW | MEDIUM | HIGH | EMERGENCY",
  "suggestion": "",
  "possible_conditions": []
}}

Patient:
Name: {data.get('name')}
Age: {data.get('age')}
Sex: {data.get('sex')}

Symptoms:
Heart Rate: {data.get('heartRate')}
Temperature: {data.get('temperature')}
Blood Pressure: {data.get('systolicBP')}/{data.get('diastolicBP')}
SpO2: {data.get('spo2')}
Pain Score: {data.get('painScore')}

Return ONLY JSON.
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    raw = response.json()["response"]
    return safe_parse(raw)