from dataclasses import dataclass, field
from typing import List, Dict, Any
from app.reasoning.patient_context import PatientContext
from app.reasoning.diagnostic_state import DiagnosticState
from app.reasoning.evidence import Evidence
from app.reasoning.clinical_state import ClinicalState

@dataclass
class ReasoningContext:

    # Patient information
    patient_profile: Dict[str, Any] = field(default_factory=dict)

    # Current verified medical state
    clinical_state: ClinicalState = field(default_factory=ClinicalState)

    # Entire conversation
    conversation_history: List[Dict[str, str]] = field(default_factory=list)

    # AI-generated rolling summary
    conversation_summary: str = ""

    # Previous AI question
    last_question: str = ""

    # Latest user message
    current_message: str = ""

    # Conversation interpretation
    interpreted_reply: Dict[str, Any] = field(default_factory=dict)

    # Clinical hypotheses
    hypotheses: List[Dict[str, Any]] = field(default_factory=list)

    # Risk assessment
    risk_assessment: Dict[str, Any] = field(default_factory=dict)

    # Planned next question
    next_question: str = ""

    # Safety alerts
    safety_alerts: List[str] = field(default_factory=list)

    patient: PatientContext = field(default_factory=PatientContext)

    diagnostic: DiagnosticState = field(default_factory=DiagnosticState)

    evidence: List[Evidence] = field(default_factory=list)