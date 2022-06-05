from models.mongotestuser.user import User, insertOne
from utils.security.hashing import Hash


def create_user(user: User):
    user.password = Hash.bcrypt(user.password)
    result = insertOne(user)
    if result:
        return {"Message": "Success"}
    else:
        return {"Message": "Failed"}
