from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
#from app.routers.blog.blog import schemas, database, models, oauth2
from library.sqlite import sqlite as database
from utils.security import oauth2
from schemas.user import user as schemas_user
from schemas.blog import blog as schemas_blog
#from blog.repository import blog
from repository.blog.create import create as create_blog
from repository.blog.read import read as read_blog
from repository.blog.update import update as update_blog
from repository.blog.delete import delete as delete_blog

router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)

get_db = database.get_db


@router.get('/', response_model=List[schemas_blog.ShowBlog])
def all(db: Session = Depends(get_db), current_user: schemas_user.User = Depends(oauth2.get_current_user)):
    return read_blog.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED,)
def create(request: schemas_blog.Blog, db: Session = Depends(get_db), current_user: schemas_user.User = Depends(oauth2.get_current_user)):
    return create_blog.create(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db), current_user: schemas_user.User = Depends(oauth2.get_current_user)):
    return delete_blog.destroy(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas_blog.Blog, db: Session = Depends(get_db), current_user: schemas_user.User = Depends(oauth2.get_current_user)):
    return update_blog.update_data(id, request, db)


@router.get('/{id}', status_code=200, response_model=schemas_blog.ShowBlog)
def show(id: int, db: Session = Depends(get_db), current_user: schemas_user.User = Depends(oauth2.get_current_user)):
    return read_blog.show(id, db)
