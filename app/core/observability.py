from prometheus_fastapi_instrumentator import Instrumentator
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from fastapi import FastAPI


def setup_observability(app: FastAPI) -> None:
    Instrumentator().instrument(app).expose(app)
    provider = TracerProvider(resource=Resource.create({SERVICE_NAME: "user-service"}))
    provider.add_span_processor(BatchSpanProcessor(ConsoleSpanExporter()))
    FastAPIInstrumentor.instrument_app(app, tracer_provider=provider)
