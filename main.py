from fastapi import FastAPI
from routers.auth import authentication
from routers.mongotestuser import user as mongotest

app = FastAPI()


app.include_router(authentication.router)

app.include_router(mongotest.router)
