from fastapi import FastAPI
#from blog import  models
from library.sqlite.sqlite import Base, engine
#from blog.database import engine
#from blog.routers import blog, user, authentication
from routers.auth import authentication
from routers.user import user
from routers.blog import blog

app = FastAPI()

# models.Base.metadata.create_all(engine)
Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
