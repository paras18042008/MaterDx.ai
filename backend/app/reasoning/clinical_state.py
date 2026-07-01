from app.reasoning.evidence import Evidence


class ClinicalState:

    def __init__(self):

        self.risk = "UNKNOWN"

        self.systems = {
            "cardiac": 0,
            "respiratory": 0,
            "neurological": 0,
            "gastrointestinal": 0,
            "musculoskeletal": 0,
        }

        self.confirmed_features = []
        self.missing_features = []
        self.red_flags = []

        self.conversation_stage = "opening"

        # -----------------------------
        # NEW ARCHITECTURE
        # -----------------------------

        self.evidence: list[Evidence] = []

        self.consultation_status = "active"

        self.chief_complaint = ""

    def to_dict(self):

        return {
            "risk": self.risk,
            "systems": self.systems,
            "confirmed_features": self.confirmed_features,
            "missing_features": self.missing_features,
            "red_flags": self.red_flags,
            "conversation_stage": self.conversation_stage,

            # New fields
            "evidence": self.evidence,
            "consultation_status": self.consultation_status,
            "chief_complaint": self.chief_complaint,
        }