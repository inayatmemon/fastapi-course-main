from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from models.mongotestuser import user as models
from utils.security import token
from utils.security.hashing import Hash
from repository.mongotestuser.read import read as getOneuser
from models.mongotestuser.user import User


router = APIRouter(tags=['Authentication'])


@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends()):
    User.name = request.username
    User.password = request.password
    user = getOneuser.find_one_user(User)
    # if not user:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                         detail=f"Invalid Credentials")
    # if not Hash.verify(user.password, request.password):
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                         detail=f"Incorrect password")
    if not user["result"]:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"Invalid Credentials")
  
    access_token = token.create_access_token(data={"sub": user["email"]})
    return {"access_token": access_token, "token_type": "bearer"}
