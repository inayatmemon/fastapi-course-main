from unittest import result
from models.mongotestuser.user import User, findOneAndUpdate


def update_user(id, user: User):
    result = findOneAndUpdate(id, user)
    if not result:
        return {"Message": "Failed"}
    else:
        return result
