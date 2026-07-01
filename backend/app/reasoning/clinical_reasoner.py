from app.reasoning.reasoning_context import ReasoningContext
from app.reasoning.evidence import Evidence
from app.reasoning.diagnostic_state import DiagnosisHypothesis

class ClinicalReasoner:

    def process(self, context: ReasoningContext) -> ReasoningContext:

        # 1. Interpret new evidence
        context = self.update_evidence(context)

        # 2. Update differential diagnosis
        context = self.update_hypotheses(context)

        # 3. Assess danger
        context = self.assess_risk(context)

        # 4. Decide next best question
        context = self.choose_next_question(context)

        # 5. Decide whether consultation can end
        context = self.check_completion(context)

        return context

    def update_evidence(self, context):

        extracted = context.extracted_features

        symptoms = extracted.get("symptoms", [])

        for symptom in symptoms:

            ev = Evidence(
            type="symptom",
            name=symptom.get("name", ""),
            value=symptom.get("severity", ""),
            source="patient",
            status="confirmed"
            )

            context.evidence.append(ev)

        return context

    def update_hypotheses(self, context):

        symptom_names = [
            e.name.lower()
            for e in context.evidence
            if e.type == "symptom"
        ]

        hypotheses = []

        if "chest pain" in symptom_names:

            hypotheses.append(
                DiagnosisHypothesis(
                    name="Acute Coronary Syndrome",
                    confidence=0.70,
                    supporting_evidence=["chest pain"],
                    missing_evidence=[
                    "shortness of breath",
                    "sweating",
                    "ecg",
                    "troponin"
                    ]
                )
            )

        context.diagnostic.hypotheses = hypotheses

        return context

    def assess_risk(self, context):
        return context

    def choose_next_question(self, context):
        return context

    def check_completion(self, context):
        return context