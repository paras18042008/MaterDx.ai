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

            current = getattr(patient_context, key, None)

    # Dictionary fields
            if isinstance(current, dict) and isinstance(value, dict):

                current.update(value)

    # List fields
            elif isinstance(current, list) and isinstance(value, list):

                current.extend(value)

    # Primitive fields
            else:

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