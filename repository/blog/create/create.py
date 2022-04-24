from fastapi import HTTPException, status
from sqlalchemy.orm import Session
#from blog import models, schemas
from models.blog import blog as models
from schemas.blog import blog as schemas


def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
