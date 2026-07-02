from app.reasoning.reasoning_context import ReasoningContext
from app.reasoning.hypothesis_generator import HypothesisGenerator


class ClinicalReasoner:

    def __init__(self):
        self.hypothesis_generator = HypothesisGenerator()

    def process(self, context: ReasoningContext) -> ReasoningContext:

        # 1. Interpret new evidence
        context = self.update_evidence(context)

        # 2. Generate differential diagnosis
        context = self.update_hypotheses(context)

        # 3. Assess danger
        context = self.assess_risk(context)

        # 4. Decide next best question
        context = self.choose_next_question(context)

        # 5. Decide whether consultation can end
        context = self.check_completion(context)

        return context

    def update_evidence(self, context):

        # Evidence has already been built by EvidenceBuilder.
        # Future versions will merge evidence, resolve conflicts,
        # update confidence, and validate incoming evidence.

        return context

    def update_hypotheses(self, context):

        context.diagnostic.hypotheses = (
            self.hypothesis_generator.generate(
                context.evidence
            )
        )

        return context

    def assess_risk(self, context):

        if not context.diagnostic.hypotheses:
            context.clinical_state.risk = "UNKNOWN"
            return context

        top = max(
            context.diagnostic.hypotheses,
            key=lambda h: h.confidence
        )

        if top.name == "Acute Coronary Syndrome":

            if top.confidence >= 0.80:
                context.clinical_state.risk = "EMERGENCY"

            elif top.confidence >= 0.60:
                context.clinical_state.risk = "HIGH"

            else:
                context.clinical_state.risk = "MODERATE"

        else:
            context.clinical_state.risk = "LOW"

        return context

    def choose_next_question(self, context):

        if not context.diagnostic.hypotheses:
            context.diagnostic.next_question = ""
            return context

        top = max(
            context.diagnostic.hypotheses,
            key=lambda h: h.confidence
        )

        if top.missing_evidence:

            missing = top.missing_evidence[0]

            questions = {
                "shortness of breath": "Are you experiencing shortness of breath?",
                "sweating": "Are you sweating?",
                "ecg": "Have you had an ECG done?",
                "troponin": "Has a troponin blood test been performed?",
            }

            context.diagnostic.next_question = questions.get(
                missing,
                f"Can you tell me more about {missing}?"
            )

        return context

    def check_completion(self, context):

        if not context.diagnostic.hypotheses:
            return context

        top = max(
            context.diagnostic.hypotheses,
            key=lambda h: h.confidence
        )

        context.diagnostic.ready_for_report = (
            top.confidence >= 0.90
            and len(top.missing_evidence) == 0
        )

        return context