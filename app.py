from fastapi import FastAPI
from agent_tools import agent

app = FastAPI()

@app.post("/chat")
def chat(message: str):

    result = agent.run_sync(message)

    return {
        "response": result.output
    }