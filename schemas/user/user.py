from typing import List, Optional
from pydantic import BaseModel
#from schemas.blog.blog import Blog


class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str
    #blogs: List[Blog] = []

    class Config():
        orm_mode = True
