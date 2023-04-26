# DevOps Apprenticeship: Project Exercise

> If you are using GitPod for the project exercise (i.e. you cannot use your local machine) then you'll want to launch a VM using the [following link](https://gitpod.io/#https://github.com/CorndelWithSoftwire/DevOps-Course-Starter). Note this VM comes pre-setup with Python & Poetry pre-installed.

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py -UseBasicParsing).Content | python -
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

## Trello setup

You'll need to create a Trello API key and token. Follow the steps [here](https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/) to do so. Once you've got those, you can add them to you `.env` file.

You'll also need to create a trello board with 3 columns named: `Things to do`, `Doing` and `Done`. You also need to get it's board ID, here's a handy [Stack Overflow thread](https://stackoverflow.com/questions/26552278/trello-api-getting-boards-lists-cards-information) to help you get it quickly. Once that's done, add it to your `.env` as well.

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Running Tests
To run the tests in Docker:

Run `docker build --target test --tag todo-app:test`

Run `docker run --env-file .env.test todo-app:test`

To run the tests directly on your machine:

Run `poetry run pytest`

## Docker Hub Todo app images

https://hub.docker.com/repository/docker/taiwoolateju/todo-app/general

## Manual deployment

Make sure you're in the root directory

Run `docker build --target production --tag todo-app:latest .`

Run `docker tag todo-app:latest taiwoolateju/todo-app:latest`

Run `docker push taiwoolateju/todo-app:latest`

Find the webhook URL for the Azure web app. This should be located in the deployment center in Azure portal for the `taiwo-todo-app`

Run `curl -dH -X POST <WEBHOOK_URL>` _Where <WEBHOOK_URL>_ is the Webhook URL in Azure portal