from sqlalchemy.orm import Session
from utils.security.hashing import Hash
from models.user import user as models
from schemas.user import user as schemas


def create(request: schemas.User, db: Session):
    new_user = models.User(
        name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
