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

### API

**Installing the dependencies**


**Running the project locally**


**Running the testing suite**


**Deploying to production**


### Cron

**Installing the dependencies**


**Running the project locally**


**Running the testing suite**


**Deploying to production**