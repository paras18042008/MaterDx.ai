import { useState } from "react";

function AIConversation({ patientProfile }) {
  const [messages, setMessages] = useState([
    {
      role: "assistant",
      content:
        "Hello! I'm MaterDx.\n\nI've received your basic information and the measurements you've entered.\n\nI'll ask a few questions to better understand your condition before connecting you with a doctor.\n\nWhat brings you in today?",
    },
  ]);

  const [input, setInput] = useState("");

  const sendMessage = async () => {
    if (!input.trim()) return;

    const updatedMessages = [
      ...messages,
      {
        role: "user",
        content: input,
      },
    ];

    setMessages(updatedMessages);
    setInput("");

    // Backend call comes in next step.
  };

  return (
    <div className="min-h-screen bg-slate-100">

      <div className="max-w-4xl mx-auto p-6">

        <h1 className="text-3xl font-bold text-blue-600 mb-6">
          MaterDx Consultation
        </h1>

        <div className="bg-white rounded-xl shadow p-4 h-[600px] overflow-y-auto">

          {messages.map((msg, index) => (
            <div
              key={index}
              className={`mb-4 flex ${
                msg.role === "assistant"
                  ? "justify-start"
                  : "justify-end"
              }`}
            >
              <div
                className={`max-w-[75%] rounded-xl p-4 whitespace-pre-wrap ${
                  msg.role === "assistant"
                    ? "bg-gray-200"
                    : "bg-blue-600 text-white"
                }`}
              >
                {msg.content}
              </div>
            </div>
          ))}

        </div>

        <div className="flex gap-3 mt-4">

          <input
            className="flex-1 border rounded-lg p-3"
            placeholder="Type your answer..."
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter") sendMessage();
            }}
          />

          <button
            onClick={sendMessage}
            className="bg-blue-600 text-white px-6 rounded-lg"
          >
            Send
          </button>

        </div>

      </div>

    </div>
  );
}

export default AIConversation;