from celery import Celery
import os

# Load environment variables
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")

celery = Celery(
    "worker",
    backend=REDIS_URL,
    broker=REDIS_URL
)

celery.conf.task_routes = {
    "app.services.tasks.*": {"queue": "default"},
}

@celery.task
def add(x, y):
    return x + y
