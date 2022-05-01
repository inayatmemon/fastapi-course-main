from models.mongotestuser.user import findAll
from utils.logger.logger import logger


def find_all_users():
    result = findAll()
    if not result:
        return {"Message": "Failed"}
    else:
        logger.info(result)
        return result
