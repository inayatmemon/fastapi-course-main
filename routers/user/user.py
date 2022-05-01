from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from library.sqlite import sqlite as database
from schemas.user import user as schemas
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
