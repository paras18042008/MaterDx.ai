from app.reasoning.evidence import Evidence

class EvidenceBuilder:

    def build(self, raw_evidence):

        evidence = []

        if not isinstance(raw_evidence, list):
            return evidence

        for item in raw_evidence:

            if not isinstance(item, dict):
                continue

            ev = Evidence(
                type=item.get("type", ""),
                name=item.get("name", ""),
                value=item.get("value"),
                unit=item.get("unit"),
                severity=item.get("severity"),
                duration=item.get("duration"),
                onset=item.get("onset"),
                location=item.get("location"),
                radiation=item.get("radiation"),
                progression=item.get("progression"),
                aggravating_factors=item.get("aggravating_factors", []),
                relieving_factors=item.get("relieving_factors", []),
                associated_features=item.get("associated_features", []),
                confidence=item.get("confidence", 1.0),
                source=item.get("source", "patient"),
                status=item.get("status", "confirmed"),
                notes=item.get("notes", "")
            )

            evidence.append(ev)

        return evidence