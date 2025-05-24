# agents/backend_dev.py

from agents.base import Agent

class BackendDev(Agent):
    def __init__(self, llm):
        super().__init__(
            name="BDeveloper",
            role="Backend Developer",
            system_message="You are a professional backend developer. Ask for more details about your assigned functions. When requested, provide API specifications and class structures for the task manager app.",
            llm_client=llm
        )
