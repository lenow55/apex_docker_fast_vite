from fastapi import FastAPI
from starlette.responses import Response

app = FastAPI()

@app.get("/")
def test():
    return Response("TEST")
