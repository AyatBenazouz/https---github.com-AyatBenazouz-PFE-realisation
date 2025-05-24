# agents/base.py

class Agent:
    def __init__(self, name, role, system_message, llm_client):
        self.name = name
        self.role = role
        self.system_message = system_message
        self.messages = [{"role": "system", "content": system_message}]
        self.llm = llm_client

    def think(self):
        """Generate and return a response using the current conversation context."""
        reply = self.llm.chat(self.messages)
        self.messages.append({"role": "assistant", "content": reply})
        return reply

    def hear(self, message):
        """Add a user message to the agent's chat history."""
        self.messages.append({"role": "user", "content": message})

    def chat(self, prompt):
        """Stateless call: send a single prompt and get a reply, without keeping context."""
        return self.llm.chat(prompt)
