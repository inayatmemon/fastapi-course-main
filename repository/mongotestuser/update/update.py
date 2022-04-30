from unittest import result
from models.mongotestuser.user import User, findOneAndUpdate
from library.mongodb.mongodb import conn
from schemas.mongottestuser.user import serializeDict


def update_user(id, user: User):
    result = findOneAndUpdate(id, user)
    if not result:
        return {"Message": "Failed"}
    else:
        return result
