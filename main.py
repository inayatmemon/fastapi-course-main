from fastapi import FastAPI
from library.sqlite.sqlite import Base, engine
from routers.auth import authentication
from routers.user import user
from routers.blog import blog
from routers.mongotestuser import user as mongotest

app = FastAPI()


Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
app.include_router(mongotest.router)
