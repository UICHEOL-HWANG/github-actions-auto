from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def test_root():
    return {"Hello":"world"}

