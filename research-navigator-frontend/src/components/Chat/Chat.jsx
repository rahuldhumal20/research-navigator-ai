import { useState } from "react";
import API from "../../services/api";

function Chat() {
  const [query, setQuery] = useState("");
  const [messages, setMessages] = useState([]);

  const sendQuery = async () => {
    if (!query) return;

    const res = await API.post("/chat", { query });

    setMessages([
      ...messages,
      { role: "user", text: query },
      { role: "ai", text: res.data.answer },
    ]);

    setQuery("");
  };

  return (
    <div className="bg-white p-5 rounded-2xl shadow-md flex flex-col">
      <h2 className="text-xl font-semibold mb-4">💬 AI Chat</h2>

      <div className="flex-1 overflow-y-auto mb-4 space-y-2 max-h-80">
        {messages.map((msg, i) => (
          <div
            key={i}
            className={`p-2 rounded-lg ${
              msg.role === "user"
                ? "bg-blue-100 text-right"
                : "bg-gray-200"
            }`}
          >
            {msg.text}
          </div>
        ))}
      </div>

      <div className="flex gap-2">
        <input
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          className="flex-1 border p-2 rounded-lg"
          placeholder="Ask something..."
        />

        <button
          onClick={sendQuery}
          className="bg-green-500 text-white px-4 rounded-lg"
        >
          Send
        </button>
      </div>
    </div>
  );
}

export default Chat;