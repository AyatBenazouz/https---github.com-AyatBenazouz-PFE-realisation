from llm.ollama_client import OllamaClient
from agents.project_manager import ProjectManager
from agents.backend_dev import BackendDev
from agents.frontend_dev import FrontendDev
import os

def log_conversation(role, content):
    with open("memory/memory.json", "a") as f:
        f.write(f"{role}:\n{content}\n\n")

def run():
    llm = OllamaClient(model="qwen")

    pm = ProjectManager(llm)
    be = BackendDev(llm)
    fe = FrontendDev(llm)

    # 1. Project Manager defines features
    pm_prompt = """
We are building a simple task manager app. Return a markdown table listing features, who is assigned (Frontend Developer or Backend Developer), and a short technical description.

Only return the table. No commentary. No suggestions. No Markdown formatting. No explanations. No motivational speech.
"""
    pm_response = pm.chat(pm_prompt)
    log_conversation("PM", f"PM:\n{pm_prompt}\n\n{pm_response}")
    print(f"\n- Project Manager:\n{pm_response}")

    # 2. Backend Developer asks for technical details
    be_question = "Can you provide technical details for my backend responsibilities?"
    be_response = be.chat(pm_response + "\n\n" + be_question)
    log_conversation("BE", f"BE:\n{be_question}\n\n{be_response}")
    print(f"\n- Backend Developer:\n{be_response}")

    # 3. Project Manager replies only to Backend Developer
    pm_to_be = """
Backend Developer asked for details. Please:
- List API endpoints
- Explain each endpoint's purpose
- Describe the data models (like User, Task)

Only respond to the Backend Developer.
"""
    pm_response_to_be = pm.chat(pm_to_be)
    log_conversation("PM", f"PM (to BE):\n{pm_response_to_be}")
    print(f"\n- Project Manager (to Backend Developer):\n{pm_response_to_be}")

    # 4. Frontend Developer asks for UI specs
    fe_question = "Can you describe what the frontend UI should look like and how it interacts with the API?"
    fe_response = fe.chat(pm_response + "\n\n" + fe_question)
    log_conversation("FE", f"FE:\n{fe_question}\n\n{fe_response}")
    print(f"\n- Frontend Developer:\n{fe_response}")

    # 5. Project Manager replies only to Frontend Developer
    pm_to_fe = """
Frontend Developer asked for UI details. Please:
- Describe the layout of the UI (HTML/CSS structure)
- Mention which API endpoints to call and when

Only respond to the Frontend Developer.
"""
    pm_response_to_fe = pm.chat(pm_to_fe)
    log_conversation("PM", f"PM (to FE):\n{pm_response_to_fe}")
    print(f"\n- Project Manager (to Frontend Developer):\n{pm_response_to_fe}")

    # 6. Backend Developer implements the API
    backend_instruction = f"""
Based on the following API description, write full backend code using FastAPI and SQLAlchemy.

Only return the code. No comments. No explanation.

{pm_response_to_be}
"""
    backend_code = be.chat(backend_instruction)
    log_conversation("BE (code)", backend_code)
    print(f"\n- Backend Developer:\n{backend_code}")

    # 7. Frontend Developer implements the UI
    frontend_instruction = f"""
Based on this backend API, write the full HTML and JavaScript frontend that interacts with it.

Only return the code. No comments. No explanation.

{backend_code}
"""
    frontend_code = fe.chat(frontend_instruction)
    log_conversation("FE (code)", frontend_code)
    print(f"\n- Frontend Developer:\n{frontend_code}")

if __name__ == "__main__":
    run()
