class EvidenceBuilder:

    def run(
        self,
        patient_context,
    ):

        interpreter_output = patient_context.interpreter_output

        if not interpreter_output:
            return patient_context

        new_information = interpreter_output.get(
            "new_information",
            {}
        )

        # Merge all extracted information into Patient Context
        for key, value in new_information.items():

            if not value:
                continue

            setattr(
                patient_context,
                key,
                value,
            )

        patient_context.missing_information = interpreter_output.get(
            "missing_information",
            []
        )

        patient_context.ambiguities = interpreter_output.get(
            "ambiguities",
            []
        )

        patient_context.interpreter_confidence = interpreter_output.get(
            "confidence",
            0.0,
        )

        return patient_context