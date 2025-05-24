 
from agents.base import Agent

class ProjectManager(Agent):
    def __init__(self, llm):
        super().__init__(
            name="Project Manager",
            role="Project Manager",
            system_message="You are a professional software project manager. Start by listing the required features for a task manager app in table format and assign responsibilities to the frontend and backend developers. Answer their questions, then request API definitions and class structure from the backend developer. Afterward, ask the frontend developer to create the HTML/CSS/JS using the backend APIs",
            llm_client=llm,
        )
