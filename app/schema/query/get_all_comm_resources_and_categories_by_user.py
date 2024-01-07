import graphene

from app.dto.all_comm_resources_and_categories_dto import (AllCommResourcesAndCategoriesDto,
                                                          serialize_all_comm_resources_and_categories)
from app.repository.user_repository import UserRepository

user_repository = UserRepository()


class GetAllCommResourcesAndCategoriesByUser(object):
    get_all_comm_resources_and_categories_by_user = (
        graphene.List(AllCommResourcesAndCategoriesDto, user_name=graphene.String()))

    def resolve_get_all_comm_resources_and_categories_by_user(self, info, user_name):
        query_result = user_repository.get_all_comm_resources_and_categories_by_user(user_name)
        return serialize_all_comm_resources_and_categories(query_result)
