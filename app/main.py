from fastapi import FastAPI, Depends
from fastapi_auth0 import Auth0
from sqlalchemy.ext.asyncio import AsyncSession
from redis import Redis
from celery import Celery
from elasticsearch import Elasticsearch
# from core.database import get_database
# from core.config import settings

app = FastAPI()

# Auth0 Setup
# auth = Auth0(domain=settings.AUTH0_DOMAIN, api_audience=settings.AUTH0_AUDIENCE)

# Redis Setup
# redis_client = Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, decode_responses=True)

# Celery Setup
# celery = Celery(__name__, broker=settings.REDIS_URL, backend=settings.REDIS_URL)

# Elasticsearch Setup
# es = Elasticsearch(settings.ELASTICSEARCH_URL)

# @app.get("/", dependencies=[Depends(auth.implicit_scheme)])
# def read_root():
#    return {"message": "Welcome to FastAPI Boilerplate!"}

# @app.get("/protected")
# def protected_route(user=Depends(auth.get_user)):
#    return {"message": "You have access", "user": user}