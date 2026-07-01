from app.reasoning.evidence_builder import EvidenceBuilder
from app.reasoning.clinical_reasoner import ClinicalReasoner


class ReasoningPipeline:

    def __init__(self):

        self.builder = EvidenceBuilder()
        self.reasoner = ClinicalReasoner()

    def process(self, context):

        # Build standardized evidence from LLM output
        context.evidence = self.builder.build(
            context.interpreted_reply.get("new_evidence", [])
        )

        # Run reasoning engine
        context = self.reasoner.process(context)

        return context