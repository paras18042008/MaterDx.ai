from app.reasoning.reasoning_context import ReasoningContext
from app.reasoning.reasoning_pipeline import ReasoningPipeline


context = ReasoningContext()

context.extracted_features = {
    "symptoms": [
        {
            "name": "chest pain",
            "severity": "severe"
        }
    ],
    "negatives": [],
    "red_flags": []
}

pipeline = ReasoningPipeline()

context = pipeline.process(context)

print("\nEvidence:")
for e in context.evidence:
    print(e)

print("\nHypotheses:")
for h in context.diagnostic.hypotheses:
    print(h)

print("\nRisk:")
print(context.clinical_state.risk)

print("\nNext Question:")
print(context.diagnostic.next_question)