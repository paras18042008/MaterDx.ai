from app.agents.conversation_interpreter import ConversationInterpreter
from app.agents.evidence_builder import EvidenceBuilder
from app.agents.doctor_agent import DoctorAgent
from app.agents.critic_agent import CriticAgent
from app.agents.judge_agent import JudgeAgent


class ReasoningPipeline:

    def __init__(self):

        self.interpreter = ConversationInterpreter()
        self.builder = EvidenceBuilder()
        self.doctor = DoctorAgent()
        self.critic = CriticAgent()
        self.judge = JudgeAgent()

    def run(self, patient_context, patient_message):

        patient_context = self.interpreter.run(
            patient_context,
            patient_message,
        )

        print("\n================ INTERPRETER OUTPUT ================\n")
        print(patient_context.interpreter_output)
        print("\n====================================================\n")
        
        patient_context = self.builder.run(
            patient_context,
    )
        print("\n========== PATIENT CONTEXT ==========\n")

        print("Chief Complaint:")
        print(patient_context.chief_complaint)

        print("\nSymptoms:")
        print(patient_context.symptoms)

        print("\nVitals:")
        print(patient_context.vitals)

        print("\nPast Medical History:")
        print(patient_context.past_medical_history)

        print("\n=====================================\n")
        print("Builder:", patient_context)

        patient_context = self.doctor.run(
            patient_context,
    )
        print("Doctor:", patient_context)

        patient_context = self.critic.run(
            patient_context,
    )
        print("Critic:", patient_context)

        patient_context = self.judge.run(
            patient_context,
    )
        print("Judge:", patient_context)

        return patient_context