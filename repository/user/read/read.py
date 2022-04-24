from sqlalchemy.orm import Session
#from blog import models, schemas
from fastapi import HTTPException, status
#from blog.hashing import Hash
from utils.security.hashing import Hash
from models.user import user as models
from schemas.user import user as schemas


def show(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")
    return user
