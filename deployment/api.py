from fastapi import FastAPI
from agents.orchestrator import execute
from safety.guard import validate_input

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Crown AI Running"}

@app.post("/predict")
def predict(input_text: str):
    if not validate_input(input_text):
        return {"error": "Invalid input"}
    return {"response": execute(input_text)}
