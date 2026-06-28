import { useState } from "react";
import PatientIntakeForm from "./PatientIntakeForm";
import AIConversation from "./AIConversation";

function App() {
  const [screen, setScreen] = useState("intake");
  const [patientData, setPatientData] = useState(null);

  const handleIntakeComplete = (data) => {
    setPatientData(data);
    setScreen("conversation");
  };

  if (screen === "intake") {
    return (
      <PatientIntakeForm
        onComplete={handleIntakeComplete}
      />
    );
  }

  return (
    <AIConversation
      patientProfile={patientData}
    />
  );
}

export default App;