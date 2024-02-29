import React, { useState } from "react";
import { askQuestion, saveQA } from "../api/api";

interface ChatComponentProps {}

const ChatComponent: React.FC<ChatComponentProps> = () => {
  const [question, setQuestion] = useState<string>("");
  const [answer, setAnswer] = useState<string>("");

  const handleLikeButtonClick = async () => {
    try {
      await saveQA(question, answer);
      console.log("Saved Q&A pair successfully.");
    } catch (error) {
      console.error("Error saving Q&A pair:", error);
    }
  };

  const handleAskButtonClick = async () => {
    try {
      const response = await askQuestion(question);
      setAnswer(response);
    } catch (error) {
      console.error("Error getting response from chatbot:", error);
    }
  };

  return (
    <div className="container mx-auto p-4">
      <label className="block mb-4">
        Question:
        <input
          type="text"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          className="border rounded px-2 py-1 w-full"
        />
      </label>
      <button
        onClick={handleAskButtonClick}
        className="bg-blue-500 text-white px-4 py-2 rounded"
      >
        Ask
      </button>
      {answer && (
        <div className="mt-4">
          <p className="font-bold">Answer:</p>
          <p className="whitespace-pre-wrap">{answer}</p>
          <button
            onClick={handleLikeButtonClick}
            className="bg-green-500 text-white px-4 py-2 rounded mt-2"
          >
            Like
          </button>
        </div>
      )}
    </div>
  );
};

export default ChatComponent;
