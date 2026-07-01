from dataclasses import dataclass, field
from typing import Any, Optional
from datetime import datetime
from uuid import uuid4


@dataclass
class Evidence:

    evidence_id: str = field(default_factory=lambda: str(uuid4()))

    # Evidence category
    type: str = ""
    # symptom
    # sign
    # vital
    # lab
    # imaging
    # medication
    # allergy
    # history
    # diagnosis
    # procedure
    # lifestyle
    # family_history
    # social_history

    # Evidence name
    name: str = ""

    # Primary value
    value: Any = None

    # Optional measurement unit
    unit: Optional[str] = None

    # Clinical qualifiers
    severity: Optional[str] = None
    duration: Optional[str] = None
    onset: Optional[str] = None
    location: Optional[str] = None
    radiation: Optional[str] = None
    progression: Optional[str] = None

    aggravating_factors: list[str] = field(default_factory=list)
    relieving_factors: list[str] = field(default_factory=list)
    associated_features: list[str] = field(default_factory=list)

    # Confidence
    confidence: float = 1.0

    # Source of evidence
    source: str = ""
    # patient
    # doctor
    # lab
    # ecg
    # imaging
    # wearable
    # ai

    # Clinical status
    status: str = "confirmed"
    # confirmed
    # denied
    # suspected
    # uncertain
    # resolved

    # Timestamp
    timestamp: datetime = field(default_factory=datetime.utcnow)

    # Free-form notes
    notes: str = ""