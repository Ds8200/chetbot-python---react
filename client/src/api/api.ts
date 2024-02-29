// api.ts
import axios, { AxiosResponse } from "axios";

interface ApiResponse {
  response: string;
}

const baseURL = "http://localhost:5000"; // יש לשנות לכתובת הבסיס של השרת

const api = axios.create({
  baseURL,
  headers: {
    "Content-Type": "application/json",
  },
});

export const askQuestion = async (question: string): Promise<string> => {
  try {
    const response: AxiosResponse<ApiResponse> = await api.post("/chat", {
      user_input: question,
    });
    return response.data.response;
  } catch (error) {
    console.error("Error getting response from chatbot:", error);
    throw error;
  }
};

export const saveQA = async (
  question: string,
  answer: string
): Promise<void> => {
  try {
    await api.post("/add_qa", { question, answer });
    console.log("Saved Q&A pair successfully.");
  } catch (error) {
    console.error("Error saving Q&A pair:", error);
    throw error;
  }
};
