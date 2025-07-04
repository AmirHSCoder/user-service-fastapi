# User Service

This is a simple FastAPI based microservice providing user management and profile features. It demonstrates database per service, clean architecture ideas and supports JWT authentication with access and refresh tokens.

The service now includes a minimal role based access control (RBAC) system. Roles
can be created and assigned to users and certain endpoints require the `admin`
role.

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

