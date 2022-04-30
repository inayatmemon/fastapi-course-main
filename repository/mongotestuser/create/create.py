from models.mongotestuser.user import User, insertOne
from library.mongodb.mongodb import mydb
from schemas.mongottestuser.user import serializeDict, serializeList
from bson import ObjectId


def create_user(user: User):
    result = insertOne(user)
    if result:
        return {"Message": "Success"}
    else:
        return {"Message": "Failed"}
    # return serializeList(collection.find())
