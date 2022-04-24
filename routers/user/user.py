from fastapi import APIRouter
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
#from app.routers.blog.blog import database, schemas, models
from library.sqlite import sqlite as database
from schemas.user import user as schemas
#from blog.repository import user
from repository.user.create import create
from repository.user.read import read


router = APIRouter(
    prefix="/user",
    tags=['Users']
)

get_db = database.get_db


@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return create.create(request, db)


@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return read.show(id, db)
