from fastapi import FastAPI
from app.routes import service_routes
from app.database.db import engine
from app.models import service_model

service_model.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(service_routes.router)

from app.models import user_model   

from app.routes import user_routes

app.include_router(user_routes.router)