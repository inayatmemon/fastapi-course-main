from bson import ObjectId
from library.mongodb.mongodb import mydb
from pydantic import BaseModel
from schemas.serializable.serializable import serializeDict, serializeList
from utils.logger.logger import logger

collection = mydb["mongousers"]


class User(BaseModel):
    name: str
    email: str
    password: str


def insertOne(user: User):
    try:
        collection.insert_one(dict(user))
        return True
    except Exception as e:
        logger.exception("Exception while insert one : ", e)
        return False


def findOneAndDelete(id, user: User):
    try:
        collection.find_one_and_delete({"_id": ObjectId(id)})
        return True
    except Exception as e:
        logger.exception("Exception while findOneAndDelete : ", e)
        return False


def findAll():
    try:
        return serializeList(collection.find())

    except Exception as e:
        logger.exception("Exception while findAll : ", e)
        return False


def findOneAndUpdate(id, user: User):
    try:
        collection.find_one_and_update({"_id": ObjectId(id)}, {
            "$set": dict(user)
        })
        return serializeDict(collection.find_one({"_id": ObjectId(id)}))

    except Exception as e:
        logger.exception("Exception while findOneAndUpdate : ", e)
        return False
