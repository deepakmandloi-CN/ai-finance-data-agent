from fastapi import FastAPI
from app.agent import run_agent

app = FastAPI(title="AI Finance Data Agent")

@app.get("/query")
def query_agent(q: str):
    try:
        return {"insight": run_agent(q)}
    except Exception as e:
        return {"error": str(e)}
