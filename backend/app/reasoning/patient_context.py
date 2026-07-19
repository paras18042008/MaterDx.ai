from dataclasses import dataclass, field
from typing import Any, List, Optional
from datetime import datetime


@dataclass
class TrackedField:
    value: Any = None
    confidence: float = 1.0
    last_updated: Optional[datetime] = None


@dataclass
class PatientContext:

    # ---------- Identity ----------
    patient_id: str = ""

    # ---------- Demographics ----------
    age: TrackedField = field(default_factory=TrackedField)
    sex_at_birth: TrackedField = field(default_factory=TrackedField)
    gender: TrackedField = field(default_factory=TrackedField)
    language: TrackedField = field(default_factory=TrackedField)
    country: TrackedField = field(default_factory=TrackedField)

    # ---------- Anthropometrics ----------
    height_cm: TrackedField = field(default_factory=TrackedField)
    weight_kg: TrackedField = field(default_factory=TrackedField)

    # ---------- Biological ----------
    pregnancy: TrackedField = field(default_factory=TrackedField)
    gestational_age_weeks: TrackedField = field(default_factory=TrackedField)
    last_menstrual_period: TrackedField = field(default_factory=TrackedField)
    menopause: TrackedField = field(default_factory=TrackedField)
    blood_group: TrackedField = field(default_factory=TrackedField)

    # ---------- Lifestyle ----------
    smoking: TrackedField = field(default_factory=TrackedField)
    alcohol: TrackedField = field(default_factory=TrackedField)
    recreational_drugs: TrackedField = field(default_factory=TrackedField)
    occupation: TrackedField = field(default_factory=TrackedField)
    exercise_level: TrackedField = field(default_factory=TrackedField)
    diet: TrackedField = field(default_factory=TrackedField)

    # ---------- Medical Background ----------
    chronic_conditions: List[str] = field(default_factory=list)
    surgeries: List[str] = field(default_factory=list)
    medications: List[str] = field(default_factory=list)
    allergies: List[str] = field(default_factory=list)

    # ---------- Family History ----------
    family_history: List[str] = field(default_factory=list)

    # ---------- Social ----------
    travel_history: List[str] = field(default_factory=list)

        # ---------- Conversation ----------
    conversation_history: List[dict] = field(default_factory=list)
    last_question: str = ""

    # ---------- Agent Outputs ----------
    interpreter_output: dict = field(default_factory=dict)
    doctor_output: dict = field(default_factory=dict)
    critic_output: dict = field(default_factory=dict)
    judge_output: dict = field(default_factory=dict)

    # ---------- Interpreter Metadata ----------
    missing_information: List[str] = field(default_factory=list)
    ambiguities: List[str] = field(default_factory=list)
    interpreter_confidence: float = 0.0

        # ---------- Current Consultation ----------

    demographics: dict = field(default_factory=dict)

    chief_complaint: List[dict] = field(default_factory=list)

    symptoms: List[dict] = field(default_factory=list)

    signs: List[dict] = field(default_factory=list)

    vitals: List[dict] = field(default_factory=list)

    past_medical_history: List[dict] = field(default_factory=list)

    surgical_history: List[dict] = field(default_factory=list)

    family_history_structured: List[dict] = field(default_factory=list)

    social_history: List[dict] = field(default_factory=list)

    occupational_history: List[dict] = field(default_factory=list)

    travel_history_structured: List[dict] = field(default_factory=list)

    lifestyle: List[dict] = field(default_factory=list)

    menstrual_history: dict = field(default_factory=dict)

    pregnancy_history: dict = field(default_factory=dict)

    immunizations: List[dict] = field(default_factory=list)

    devices: List[dict] = field(default_factory=list)

    lab_results: List[dict] = field(default_factory=list)

    imaging: List[dict] = field(default_factory=list)

    procedures: List[dict] = field(default_factory=list)

    risk_factors: List[dict] = field(default_factory=list)

    red_flags: List[dict] = field(default_factory=list)

    negated_findings: List[dict] = field(default_factory=list)

    uncertain_findings: List[dict] = field(default_factory=list)

    timeline: List[dict] = field(default_factory=list)