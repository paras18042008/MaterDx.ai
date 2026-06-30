from app.reasoning.feature_extractor import extract_features
from app.reasoning.conversation_interpreter import interpret_reply
from app.reasoning.clinical_updater import update_state
from app.reasoning.question_planner import get_next_question


class ConversationManager:

    def process_turn(
        self,
        state,
        user_message,
        previous_question=None,
    ):

        # Step 1
        extracted = extract_features(user_message)

        # Step 2
        interpretation = None

        if previous_question:
            interpretation = interpret_reply(
                previous_question,
                user_message,
            )

        # Step 3
        state = update_state(
            state,
            extracted,
        )

        # Step 4
        next_question = get_next_question(state)

        return {
            "state": state,
            "extracted": extracted,
            "interpretation": interpretation,
            "next_question": next_question,
        }