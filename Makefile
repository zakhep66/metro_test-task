DC = docker compose
EXEC = docker exec -it
LOGS = docker logs
ENV = --env-file .env
APP_FILE = docker_compose/app.yaml
STORAGE_FILE = docker_compose/storage.yaml
APP_CONTAINER = app

.PHONY: app
app:
	${DC} -f ${APP_FILE} -f ${STORAGE_FILE} ${ENV} up --build -d

.PHONY: app-logs
app-logs:
	${LOGS} ${APP_CONTAINER} -f

.PHONY: app-down
app-down:
	${DC} -f ${APP_FILE} -f ${STORAGE_FILE} down

.PHONY: app-bash
app-bash:
	${EXEC} ${APP_CONTAINER} bash

.PHONY: app-migrations
app-migrations:
	${EXEC} ${APP_CONTAINER} alembic revision --autogenerate

.PHONY: app-rollback
app-rollback:
	${EXEC} ${APP_CONTAINER} alembic downgrade -1

.PHONY: app-migrate
app-migrate:
	${EXEC} ${APP_CONTAINER} alembic upgrade head