import { useState } from "react";
import api from "../services/api";

export default function IntakeLoop() {
  const [state, setState] = useState({});
  const [questions, setQuestions] = useState([
    "Do you have chest pain?"
  ]);
  const [currentQ, setCurrentQ] = useState(0);
  const [loading, setLoading] = useState(false);

const handleAnswer = async (answer) => {
  const updatedState = {
    ...state,
    [`q_${currentQ}`]: answer
  };

  setState(updatedState);
  setLoading(true);

  try {
    const response = await api.post("/classify", updatedState);

    console.log("Backend response:", response.data);

    const nextQs = response.data.next_questions;

    if (nextQs && nextQs.length > 0) {
      setQuestions(nextQs);
      setCurrentQ(0);
    } else {
      setQuestions(["Assessment Complete"]);
      setCurrentQ(0);
    }

  } catch (err) {
    console.error("API error:", err);
  }

  setLoading(false);
};

  return (
    <div style={{ padding: 20, fontFamily: "Arial" }}>
      <h2>MaterDx Intake</h2>

      <h3>{questions[currentQ]}</h3>

      {loading && <p>Analyzing...</p>}

      {!loading && questions[currentQ] !== "Assessment Complete" && (
        <div>
          <button onClick={() => handleAnswer("High")}>High</button>
          <button onClick={() => handleAnswer("Medium")}>Medium</button>
          <button onClick={() => handleAnswer("Low")}>Low</button>
          <button onClick={() => handleAnswer("None")}>None</button>
        </div>
      )}

      {questions[currentQ] === "Assessment Complete" && (
        <pre>{JSON.stringify(state, null, 2)}</pre>
      )}
    </div>
  );
}