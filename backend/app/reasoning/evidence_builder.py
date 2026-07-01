from app.reasoning.evidence import Evidence


class EvidenceBuilder:

    def build(self, extracted):

        evidence = []

        # -----------------------------
        # Symptoms
        # -----------------------------
        for symptom in extracted.get("symptoms", []):

            evidence.append(
                Evidence(
                    type="symptom",
                    name=symptom.get("name", ""),
                    value=symptom.get("severity", ""),
                    source="patient",
                    status="confirmed"
                )
            )

        # -----------------------------
        # Negative symptoms
        # -----------------------------
        for symptom in extracted.get("negatives", []):

            evidence.append(
                Evidence(
                    type="symptom",
                    name=symptom,
                    source="patient",
                    status="denied"
                )
            )

        # -----------------------------
        # Red flags
        # -----------------------------
        for flag in extracted.get("red_flags", []):

            evidence.append(
                Evidence(
                    type="red_flag",
                    name=flag,
                    source="patient",
                    status="confirmed"
                )
            )

        return evidence