from app.reasoning.diagnostic_state import DiagnosisHypothesis


class HypothesisGenerator:

    def generate(self, evidence):

        symptom_names = {
            e.name.lower()
            for e in evidence
            if e.type == "symptom"
        }

        hypotheses = []

        if "chest pain" in symptom_names or "chest_pain" in symptom_names:
            hypotheses.append(
                DiagnosisHypothesis(
                    name="Acute Coronary Syndrome",
                    confidence=0.70,
                    supporting_evidence=["chest pain"],
                    contradicting_evidence=[],
                    missing_evidence=[
                        "shortness of breath",
                        "sweating",
                        "ecg",
                        "troponin"
                    ]
                )
            )

            hypotheses.append(
                DiagnosisHypothesis(
                    name="Gastroesophageal Reflux Disease",
                    confidence=0.30,
                    supporting_evidence=["chest pain"],
                    contradicting_evidence=[],
                    missing_evidence=[
                        "burning sensation",
                        "acid reflux"
                    ]
                )
            )

            hypotheses.append(
                DiagnosisHypothesis(
                    name="Costochondritis",
                    confidence=0.25,
                    supporting_evidence=["chest pain"],
                    contradicting_evidence=[],
                    missing_evidence=[
                        "pain on palpation"
                    ]
                )
            )

        return hypotheses