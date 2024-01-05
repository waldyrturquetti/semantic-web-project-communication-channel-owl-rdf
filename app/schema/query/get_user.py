import graphene

from app.repository.user_repository import UserRepository
from app.model.user_entity import User

user_repository = UserRepository()

class GetUser(object):
    get_user = graphene.Field(User, name=graphene.String())

    def resolve_get_user(self, info, name):
        return user_repository.get_user_by_name(name)