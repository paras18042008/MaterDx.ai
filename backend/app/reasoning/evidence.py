from dataclasses import dataclass, field
from typing import Any, Optional
from datetime import datetime
from uuid import uuid4


@dataclass
class Evidence:

    evidence_id: str = field(default_factory=lambda: str(uuid4()))

    # What kind of evidence?
    type: str = ""
    # symptom, sign, lab, imaging, ecg,
    # medication, history, vital, physical_exam ...

    name: str = ""

    value: Any = None

    unit: Optional[str] = None

    confidence: float = 1.0

    source: str = ""
    # patient
    # doctor
    # lab
    # ecg
    # wearable
    # ai

    status: str = "confirmed"
    # confirmed
    # denied
    # suspected
    # unknown

    timestamp: datetime = field(default_factory=datetime.utcnow)

    notes: str = ""