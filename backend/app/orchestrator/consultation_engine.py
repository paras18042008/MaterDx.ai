from app.agents.conversation_interpreter import ConversationInterpreter
from app.agents.evidence_builder import EvidenceBuilder
from app.agents.doctor_agent import DoctorAgent
from app.agents.critic_agent import CriticAgent
from app.agents.judge_agent import JudgeAgent


class ConsultationEngine:

    def __init__(self):

        self.interpreter = ConversationInterpreter()

        self.builder = EvidenceBuilder()

        self.doctor = DoctorAgent()

        self.critic = CriticAgent()

        self.judge = JudgeAgent()

    def run(
        self,
        patient_context,
        patient_message,
    ):

        # Step 1
        patient_context = self.interpreter.run(
            patient_context,
            patient_message,
        )

        # Step 2
        patient_context = self.builder.run(
            patient_context,
        )

        # Step 3
        patient_context = self.doctor.run(
            patient_context,
        )

        # Step 4
        patient_context = self.critic.run(
            patient_context,
        )

        # Step 5
        patient_context = self.judge.run(
            patient_context,
        )

        return patient_context