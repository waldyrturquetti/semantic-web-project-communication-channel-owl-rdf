import graphene

from app.dto.user_contacts_relationships_dto import UserContactsRelationshipDto
from app.repository.user_repository import UserRepository

user_repository = UserRepository()


class GetUserContactsRelationship(object):
    get_user_contacts_by_user = (
        graphene.List(UserContactsRelationshipDto, name=graphene.String()))

    def resolve_get_user_contacts_by_user(self, info, name):
        return user_repository.get_user_contacts_by_user(name)
