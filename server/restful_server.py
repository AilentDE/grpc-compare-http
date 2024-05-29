from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class HelloRequest(BaseModel):
    name: str

@app.post("/hello")
async def say_hello(request: HelloRequest):
    return {"message": f"Hello, {request.name}!"}

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
