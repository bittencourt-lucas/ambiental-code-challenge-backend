# Code Challenge - Ambiental Media

This project contains a MonoRepo for two different projects:

- An API that provides two endpoints.
- A crontab running a workflow every 5 minutes to gather, process, and store data.

## Objective

The main goal with this project is to display an array of Software Engineering skills using Python.

The objective is to gather, process, and store forecast data every 5 minutes. This data can then be retrieved using two endpoints, as described:

> `/previsao` returns a forecast of wind speed and direction for the next 7 days.
>
> `/alerta` returns the high risk wind speed schedule for the next 7 days.

## Solution

As mentioned, the solution was divided in two different projects, API and Cron.

> `API` is a microservice running on FastAPI that makes the endpoints mentioned available.
>
> `Cron` is a microservice that runs a cronjob with a workflow every 5 minutes. The workflow is responsible for gathering the forecast data, processing it to fit the conditions established, and storing it in a NoSQL database (Google Firestore, in this case).

### Easy Mode

> This is the most straightforward way to run the project.

1. Make sure you have a file containing Google Application Credentials located at `credentials/gcp-credentials.json`.

2. You must also have Docker and Docker Compose installed in your computer.

3. Run `docker-compose build` and `docker-compose up -d`.

### API

**Installing the dependencies**

> Make sure you have Python >= 3.10 installed.

To install the requirements for both projects, run `pip install -r requirements.txt`.

**Running the project locally**

To run the project locally, first, make sure you create a `.env` file based on `.env.example`.

After you have configured the environment variables properly, move into the API folder with `cd api/`.

Finally, run `uvicorn main:app --reload`.

**Running the testing suite**

To run the testing suite, make sure you have the requirements installed. Then, you can just run `pytest api`.

**Running the project in a container**

Build the project image:

`docker build -f Dockerfile.api -t api-python:latest .`

Create the project container:

`docker run --name weather-app -p 8000:8000 -d api-python:latest`

### Cron

**Installing the dependencies**
> Make sure you have cron installed on your environment. If you are using Arch Linux, you can install it with `sudo pacman -S cronie`.

> Make sure you have Python >= 3.10 installed.

To install the requirements for both projects, run `pip install -r requirements.txt`.

**Running the project locally**

To run the project locally, first, make sure you create a `.env` file based on `.env.example`.

After you have configured the environment variables properly, you need simply run `python cron/main.py`.

**Running the testing suite**

To run the testing suite, make sure you have the requirements installed. Then, you can just run `pytest cron`.

**Running the project in a container**

Build the project image:

`docker build -f Dockerfile.cron -t cron-python:latest .`

Create the project container:

`docker run --name cron-app -d cron-python:latest`

## Questions & Comments

You can contact me through my email `lucsacafieiro@gmail.com`.
