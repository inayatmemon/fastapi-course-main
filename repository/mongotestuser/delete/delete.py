from models.mongotestuser.user import User, findOneAndDelete
from library.mongodb.mongodb import conn
from schemas.mongottestuser.user import serializeDict, serializeList


def delete_user(id, user: User):
    result = findOneAndDelete(id, user)
    if result:
        return {"Message": "Success"}
    else:
        return {"Message": "Failed"}
    # return serializeDict(conn.local.user.find_one_and_delete({"_id": ObjectId(id)}))
