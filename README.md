# Django Clean Architecture Approach

A reference project demonstrating **Clean Architecture** with Django: domain-driven design, use cases, and clear separation between domain, application, and infrastructure layers.

## Goal

This project aims to:

- **Show a practical Clean Architecture** applied to Django: domain entities, application use cases, and infrastructure (repositories, Django ORM) kept in separate layers.
- **Combine multiple interfaces**: REST (Django REST Framework), gRPC (django-grpc-framework), with optional FastAPI in the future.
- **Provide a production-style setup**: PostgreSQL, Kafka (Redpanda), Schema Registry, Prometheus, and Grafana for observability.

It serves as a template for building maintainable, testable Django services where business logic lives in the domain and application layers, independent of web and database details.

## Technologies

| Category        | Stack                          |
|----------------|---------------------------------|
| **Framework**  | Django 4.x, Django REST Framework |
| **API**        | REST, gRPC (django-grpc-framework) |
| **Database**   | PostgreSQL                      |
| **Messaging**  | Kafka (Redpanda), Schema Registry |
| **Observability** | Prometheus, Grafana         |
| **Testing**    | pytest, pytest-django, freezegun |
| **Code quality** | black, flake8, mypy, pre-commit |

*Planned: FastAPI, Express/NestJS (optional).*

---

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) and Docker Compose
- [Task](https://taskfile.dev/) (optional but recommended for run/build/stop commands)
- Python 3.10+ (for running tests locally)

## How to Run

### Using Task (recommended)

From the project root:

```bash
# Build images and start all services (Postgres, Kafka, Schema Registry, Product app)
task run

# Or: build once, then only start
task build
task up
```

Services:

- **Product API (Django)**: http://localhost:8000
- **Prometheus**: http://localhost:9090
- **Grafana**: http://localhost:3000
- **PostgreSQL**: localhost:5432 (user/password: `postgres`/`postgres`)

Stop everything:

```bash
task stop
```

Other useful commands:

```bash
task logs          # All services logs
task logs:product  # Product service logs only
task product       # Shell into the product container
```

### Using Docker Compose directly

```bash
docker-compose build --no-cache
docker-compose up -d postgres product
# Optional: add kafka schema-registry prometheus grafana
```

### Environment variables

Create a `.env` file in the project root if needed. The app expects (or uses defaults for):

- `POSTGRES_HOST`, `POSTGRES_USER`, `POSTGRES_USER_PWD`, `POSTGRES_DB` for the database.

For tests, a `.env.test` can be used (see Taskfile `dotenv`).

### Running the Django app locally (no Docker)

```bash
cd product
python -m venv venv
source venv/bin/activate   # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
# Set DB to local Postgres or use SQLite for quick checks
export DJANGO_SETTINGS_MODULE=setup.settings
python manage.py runserver
```

---

## How to Test

Tests are written with **pytest** and **pytest-django**. Configuration is in `product/pytest.ini`.

From the **project root**:

```bash
cd product
pytest
```

Or from the `product` directory:

```bash
pytest
```

Useful options:

```bash
pytest -v                    # Verbose
pytest product/              # Only product package
pytest -k "test_create"      # Match test name
pytest --tb=short            # Shorter tracebacks
```

Ensure `DJANGO_SETTINGS_MODULE=setup.settings` is set (pytest.ini already sets it). For integration tests that need the DB, have PostgreSQL available or use the test settings if defined.

---

## Project structure (Clean Architecture)

```
product/
├── manage.py
├── setup/                 # Django project (settings, urls, wsgi)
├── product/               # Core (Clean Architecture)
│   ├── domain/            # Entities, value objects, validators, errors
│   ├── application/       # Use cases, DTOs, ports (interfaces)
│   └── infra/             # Repository implementations (e.g. Django ORM)
├── django_app/            # Django app: models, admin, HTTP/gRPC adapters
├── proto/                 # gRPC protos and generated code
└── __tests__/             # Integration/API tests
```

- **Domain**: business rules and entities (e.g. `Product`).
- **Application**: use cases that orchestrate domain and call repositories.
- **Infra**: concrete implementations (DB, Kafka, etc.).
- **django_app**: adapters that expose use cases via REST and gRPC.

---

## How to Contribute

1. **Fork** the repository and clone your fork.
2. **Create a branch** for your change: `git checkout -b feature/my-feature` or `fix/my-fix`.
3. **Set up the environment**:
   - Install pre-commit: `pip install pre-commit && pre-commit install`
   - Run tests: `cd product && pytest`
4. **Make your changes**:
   - Follow the existing structure (domain → application → infra/adapters).
   - Add or update tests as needed.
   - Format and lint: the repo uses **black**, **flake8**, and **mypy** (see `requirements.txt`).
5. **Commit** with clear messages and ensure pre-commit passes.
6. **Push** to your fork and open a **Pull Request** against the main repository.
7. In the PR description, explain the goal of the change and how it was tested.

By contributing, you agree that your contributions may be used under the same license as the project.
