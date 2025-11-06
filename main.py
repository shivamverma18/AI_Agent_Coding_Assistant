from fastapi import FastAPI
from pydantic import BaseModel
from ai_engine import explain_code, debug_code, generate_code

app = FastAPI()

class CodeRequest(BaseModel):
    language: str
    topic: str
    level: str

@app.post("/explain")
def explain(data: CodeRequest):
    return {"response": explain_code(data.language, data.topic, data.level)}

@app.post("/debug")
def debug(data: CodeRequest):
    response = debug_code(data.language, data.topic)
    return {"response": response}

@app.post("/generate")
def generate(data: CodeRequest):
    return {"response": generate_code(data.language, data.topic, data.level)}
