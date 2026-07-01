from dataclasses import dataclass, field
from typing import List


@dataclass
class DiagnosisHypothesis:
    name: str
    confidence: float = 0.0
    supporting_evidence: List[str] = field(default_factory=list)
    contradicting_evidence: List[str] = field(default_factory=list)
    missing_evidence: List[str] = field(default_factory=list)


@dataclass
class DiagnosticState:

    # Ranked differential diagnoses
    hypotheses: List[DiagnosisHypothesis] = field(default_factory=list)

    # Dangerous diagnoses that must not be missed
    dangerous_conditions: List[str] = field(default_factory=list)

    # Overall confidence in the reasoning
    diagnostic_confidence: float = 0.0

    # Highest-value information still needed
    information_needed: List[str] = field(default_factory=list)

    # Next question to ask
    next_question: str = ""

    # Whether AI has enough information
    ready_for_report: bool = False