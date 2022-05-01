from models.mongotestuser.user import User, insertOne


def create_user(user: User):
    result = insertOne(user)
    if result:
        return {"Message": "Success"}
    else:
        return {"Message": "Failed"}
