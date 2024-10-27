import os
from fastapi import FastAPI, HTTPException, Form
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

# Endpoint for loading HTML form
@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("calc.html", "r") as file:
        return file.read()

# Endpoint for performing calculations
@app.post("/calculate")
async def calculate(num1: float = Form(...), operation: str = Form(...), num2: float = Form(...)):
    if operation == "plus":
        return {"result": num1 + num2}
    elif operation == "minus":
        return {"result": num1 - num2}
    elif operation == "times":
        return {"result": num1 * num2}
    elif operation == "divided":
        if num2 == 0:
            raise HTTPException(status_code=400, detail="Division by zero is not allowed.")
        return {"result": num1 / num2}
    else:
        raise HTTPException(status_code=400, detail="Invalid operation.")

# Run the app with a specified or default port
if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # Default to 8000 if PORT not set
    uvicorn.run(app, host="0.0.0.0", port=port)
