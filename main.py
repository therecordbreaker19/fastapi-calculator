from fastapi import FastAPI, HTTPException, Form
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    try:
        # Ensure "calc.html" is in the same directory or specify the correct path
        with open("calc.html", "r") as file:
            return file.read()
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="calc.html not found")

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

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))  # Defaults to 8000 if PORT is not set
    uvicorn.run(app, host="0.0.0.0", port=port)
