# Airflow Template


Bootstrap a local Airflow 3 environment - fast.

``` pip install angreal && angreal init https://github.com/angreal/airflow.git ```

The template targets Airflow `3.3.2` by default (set `airflow_version` when you render it).
It needs Python 3.10 or newer, Docker, and Docker Compose v2 (`docker compose`).

## Features

```
demo: commands for controlling the demo environment
  clean - shut down services and remove files
  restart - restart all service
  start - start services for example dags
  stop - stop services for example dags
dev-setup - setup a development environment
test: commands for executing tests
  lint - lint our project
  run - run our test suite. default is unit tests only
```

- `angreal demo start` builds the image from `dev/Dockerfile` and starts the stack in
  `dev/docker-compose.yaml` (based on the official Airflow 3 compose file): Postgres,
  the API server, the scheduler, the DAG processor and the triggerer, with the
  LocalExecutor. The UI and API answer on http://localhost:8080 (user `airflow`,
  password `airflow`); set `AIRFLOW_API_PORT` to use another port.
- `angreal test run` runs the unit tests; `--integrity` runs the DAG integrity tests
  (import errors and deprecation warnings); `--full` runs both.
- `angreal test lint` runs pre-commit, including ruff's Airflow 3 rules (`AIR3`).

Airflow 2 users can render an older commit of this template.
