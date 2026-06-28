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

    def to_dict(self):
        return {
            "risk": self.risk,
            "systems": self.systems,
            "confirmed_features": self.confirmed_features,
            "missing_features": self.missing_features,
            "red_flags": self.red_flags,
            "conversation_stage": self.conversation_stage,
        }