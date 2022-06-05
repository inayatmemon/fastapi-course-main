from models.mongotestuser.user import findAll, findOne,User
from utils.logger.logger import logger


def find_all_users():
    result = findAll()
    if not result:
        return {"Message": "Failed"}
    else:
        logger.info(result)
        return result

def find_one_user(user: User):
    result = findOne(user)
    if not result:
        return {"Message": "Failed"}
    else:
        logger.info(result)
        return result
