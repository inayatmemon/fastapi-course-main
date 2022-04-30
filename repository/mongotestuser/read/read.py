from models.mongotestuser.user import findAll
from library.mongodb.mongodb import conn
from schemas.mongottestuser.user import serializeList
from bson import ObjectId


def find_all_users():
    result = findAll()
    if not result:
        return {"Message": "Failed"}
    else:
        return result
