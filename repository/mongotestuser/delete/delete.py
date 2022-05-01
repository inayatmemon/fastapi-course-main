from models.mongotestuser.user import User, findOneAndDelete


def delete_user(id, user: User):
    result = findOneAndDelete(id, user)
    if result:
        return {"Message": "Success"}
    else:
        return {"Message": "Failed"}
