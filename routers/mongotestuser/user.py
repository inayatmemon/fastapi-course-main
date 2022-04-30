from fastapi import APIRouter
from models.mongotestuser.user import User
from repository.mongotestuser.create.create import create_user
from repository.mongotestuser.update.update import update_user
from repository.mongotestuser.delete.delete import delete_user
from repository.mongotestuser.read.read import find_all_users

router = APIRouter(
    prefix="/mongo",
    tags=['Mongo']
)


@router.get('/')
async def find_all():
    return find_all_users()

    # @User.get('/{id}')
    # async def find_one_User(id):
    #     return serializeDict(conn.local.User.find_one({"_id":ObjectId(id)}))


@router.post('/')
async def create(user: User):
    res = create_user(user)
    return res


@router.put('/{id}')
async def update(id, user: User):
    res = update_user(id, user)
    return res


@router.delete('/{id}')
async def delete(id, user: User):
    return delete_user(id, user)
