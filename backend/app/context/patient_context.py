from dataclasses import dataclass, field


@dataclass
class PatientContext:

    # Session
    session_id: str = ""

    # Patient profile
    age: int | None = None
    sex: str | None = None

    # Main complaint
    chief_complaint: str = ""

    # Structured evidence
    evidence: list = field(default_factory=list)

    # Differential diagnosis
    hypotheses: list = field(default_factory=list)

    # Current risk
    risk: str = "UNKNOWN"

    # Questions

    questions_asked: list = field(default_factory=list)

    next_question: str = ""

    # Completion

    ready_for_report: bool = False

    # Internal reasoning memory

    doctor_output: dict = field(default_factory=dict)

    critic_output: dict = field(default_factory=dict)

    judge_output: dict = field(default_factory=dict)