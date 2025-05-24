# agents/frontend_dev.py

from agents.base import Agent

class FrontendDev(Agent):
    def __init__(self, llm_client):
        super().__init__(
            name="FDeveloper",
            role="Frontend Developer",
            system_message="You are a professional frontend developer. Ask for more details about your assigned functions. Once APIs are available, create open HTML, CSS, and JS code that uses them.",
            llm_client=llm_client
        )
