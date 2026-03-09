from fastapi import FastAPI
import database
import models
from routers import users
from routers import tasks

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])