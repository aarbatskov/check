import os
from time import sleep

from celery import Celery

backend_url = os.getenv("BACKEND_URL")
broker_url = os.getenv("BROKER_URL")

app = Celery()


@app.task(name='my_task')
def execute():
    sleep(500)
    return True

