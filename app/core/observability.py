from prometheus_fastapi_instrumentator import Instrumentator
from fastapi import FastAPI


def setup_observability(app: FastAPI) -> None:
    Instrumentator().instrument(app).expose(app)
