from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise import Tortoise

from src.database.config import TORTOISE_ORM
from src.database.register import register_tortoise
from src.env import get_debug, get_root, get_url

Tortoise.init_models(["src.database.models"], "models")

app = FastAPI(root_path=get_root())

app.add_middleware(
    CORSMiddleware,
    allow_origins=[get_url()],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from src.routes import diagrams, records

app.include_router(diagrams.router)
app.include_router(records.router)


@app.get("/")
def test():
    return "TEST"


register_tortoise(app, config=TORTOISE_ORM, generate_schemas=False)


debug = get_debug()
print(debug)
if debug is True:
    import logging
    import sys

    from tortoise.log import db_client_logger, logger

    print("DEBUG MODE")
    fmt = logging.Formatter(
        fmt="%(asctime)s - %(name)s:%(lineno)d - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    sh = logging.StreamHandler(sys.stdout)
    sh.setLevel(logging.DEBUG)
    sh.setFormatter(fmt)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(sh)
    db_client_logger.setLevel(logging.DEBUG)
    db_client_logger.addHandler(sh)
