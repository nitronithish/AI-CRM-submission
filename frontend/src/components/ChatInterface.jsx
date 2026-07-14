import { useState } from "react";
import axios from "axios";

function ChatInterface() {
  const [message, setMessage] = useState("");
  const [reply, setReply] = useState("");

  const sendToAI = async () => {
    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/chat",
        {
          message: message,
        }
      );

      setReply(response.data.reply);
    } catch (error) {
      setReply("Error connecting to backend");
    }
  };

  return (
    <div style={{ marginTop: "20px" }}>
      <h3>AI Chat Assistant</h3>

      <textarea
        placeholder="Describe your meeting with the doctor..."
        rows="6"
        cols="60"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      ></textarea>

      <br />
      <br />

      <button onClick={sendToAI}>Send to AI</button>

      <br />
      <br />

      <h3>AI Reply</h3>
      <p>{reply}</p>
    </div>
  );
}

export default ChatInterface;