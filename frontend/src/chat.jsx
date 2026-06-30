import { useState } from "react";

function Chat() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const session_id = "test1"; // later we can make this dynamic

  const sendMessage = async () => {
    
    console.log("SEND BUTTON CLICKED");

    if (!input.trim()) return;

    const userMessage = input;

    // add user message immediately
    setMessages((prev) => [
      ...prev,
      { role: "user", text: userMessage },
    ]);

    setInput("");
    setLoading(true);

    try {
      const res = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
  session_id: "test1",
  message: userMessage,
})
      });

      if (!res.ok) {
        throw new Error("Server error");
      }

      const data = await res.json();

      console.log("AI RESPONSE:", data);

      // add AI response
      setMessages((prev) => [
        ...prev,
        {
          role: "ai",
          text: data.next_question || "No response",
        },
      ]);
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        {
          role: "ai",
          text: "Error connecting to server",
        },
      ]);
      console.error(err);
    }

    setLoading(false);
  };

  return (
    <div style={styles.container}>
      <h2 style={styles.header}>MaterDx AI Chat</h2>

      {/* CHAT WINDOW */}
      <div style={styles.chatBox}>
        {messages.map((msg, idx) => (
          <div
            key={idx}
            style={{
              ...styles.message,
              alignSelf: msg.role === "user" ? "flex-end" : "flex-start",
              backgroundColor:
                msg.role === "user" ? "#DCF8C6" : "#F1F0F0",
            }}
          >
            {msg.text}
          </div>
        ))}

        {loading && (
          <div style={styles.typing}>AI is thinking...</div>
        )}
      </div>

      {/* INPUT AREA */}
      <div style={styles.inputBox}>
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Describe your symptoms..."
          style={styles.input}
          onKeyDown={(e) => e.key === "Enter" && sendMessage()}
        />

        <button onClick={sendMessage} style={styles.button}>
          Send
        </button>
      </div>
    </div>
  );
}

const styles = {
  container: {
    maxWidth: "700px",
    margin: "0 auto",
    padding: "20px",
    fontFamily: "Arial",
  },

  header: {
    textAlign: "center",
    marginBottom: "15px",
  },

  chatBox: {
    height: "400px",
    border: "1px solid #ddd",
    borderRadius: "10px",
    padding: "10px",
    display: "flex",
    flexDirection: "column",
    overflowY: "auto",
    marginBottom: "10px",
  },

  message: {
    padding: "10px",
    borderRadius: "10px",
    margin: "5px 0",
    maxWidth: "70%",
    fontSize: "14px",
  },

  typing: {
    fontSize: "12px",
    color: "gray",
    fontStyle: "italic",
  },

  inputBox: {
    display: "flex",
    gap: "10px",
  },

  input: {
    flex: 1,
    padding: "10px",
    borderRadius: "8px",
    border: "1px solid #ccc",
  },

  button: {
    padding: "10px 20px",
    backgroundColor: "#007bff",
    color: "white",
    border: "none",
    borderRadius: "8px",
    cursor: "pointer",
  },
};

export default Chat;