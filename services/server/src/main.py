from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes import diagrams, records


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(diagrams.router)
app.include_router(records.router)

@app.get("/")
def test():
    return "TEST"

@app.get("/home")
def test2():
    return "TEST2"
