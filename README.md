# User Service

This is a simple FastAPI based microservice providing user management and profile features. It demonstrates database per service, clean architecture ideas and supports JWT authentication with access and refresh tokens.

## Development

### Requirements
- Python 3.11+
- PostgreSQL

### Running locally

```bash
pip install -r requirements.txt  # install dependencies
uvicorn app.main:app --reload
```

### Tests

Run unit tests with pytest:

```bash
pytest -q
```

### Container

You can build and run the service with docker-compose:

```bash
docker-compose up --build
```

