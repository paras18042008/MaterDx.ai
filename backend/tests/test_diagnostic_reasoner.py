from app.reasoning.diagnostic_reasoner import DiagnosticReasoner

reasoner = DiagnosticReasoner()

evidence = [
    {
        "type": "symptom",
        "name": "chest pain",
        "severity": "severe",
        "location": "left chest",
        "radiation": "left arm",
        "duration": "since this morning"
    }
]

result = reasoner.reason(evidence)

print(result)