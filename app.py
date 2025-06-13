from fastapi import FastAPI
from langserve import add_routes
from langchain_core.runnables import RunnableLambda
from pydantic import BaseModel

app = FastAPI()

# Basit zincir
def simple_func(inputs: dict) -> str:
    return f"Hello in {inputs['language']}: {inputs['text']}"

chain = RunnableLambda(simple_func)

# Girdi modeli
class InputModel(BaseModel):
    language: str
    text: str

add_routes(app, chain, path="/chain", input_schema=InputModel)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)
