import os
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
DATABASE_URL = os.getenv("DATABASE_URL")
print("databaseConfigured=" + str(bool(DATABASE_URL)), flush=True)
app = FastAPI()
@app.get("/", response_class=PlainTextResponse)
def hello():
    return "Hello dummy-fastapi"
@app.get("/health")
def health():
    return {"ok": True, "app": "dummy-fastapi"}
