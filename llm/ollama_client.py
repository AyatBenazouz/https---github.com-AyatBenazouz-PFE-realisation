
import requests

class OllamaClient:
    def __init__(self, model="qwen"):
        self.model = model

    def chat(self, prompt):
        messages = [{"role": "user", "content": prompt}]

        response = requests.post(
            "http://localhost:11434/api/chat",
            json={
                "model": self.model,
                "messages": messages,
                "stream": False
            },
        )

        try:
            data = response.json()
            if "message" in data and "content" in data["message"]:
                return data["message"]["content"]
            else:
                print("❌ Unexpected response structure:")
                print(data)
                raise KeyError("Expected key 'message' not found in Ollama response")
        except Exception as e:
            print("❌ Error while parsing Ollama response:", e)
            print("Raw response text:", response.text)
            raise
