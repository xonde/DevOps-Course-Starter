FROM python:slim-buster as base

WORKDIR /

RUN apt-get update
RUN apt-get install -y curl

RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="${PATH}:/root/.local/bin"
ENV PATH="${PATH}:/root/.local/share/pypoetry/venv/bin/"

COPY pyproject.toml poetry.toml /exercise_five/
WORKDIR /exercise_five

RUN poetry install

COPY todo_app/ /exercise_five/todo_app

EXPOSE 5000

# Development

FROM base as development
ENTRYPOINT poetry run flask run --host 0.0.0.0

# Production

FROM base as production
ENTRYPOINT poetry run gunicorn --bind 0.0.0.0 "todo_app.app:create_app()"


# ENTRYPOINT [ "tail", "-f", "/dev/null" ]
# Run Dev with:
# docker run --env-file ./.env -p 5000:5000 --mount type=bind,source="$(pwd)"/todo_app,target=/exercise_five/todo_app todo-app:dev