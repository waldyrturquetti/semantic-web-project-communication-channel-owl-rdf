import graphene

from app.dto.all_comm_resources_and_categories_dto import (AllCommResourcesAndCategoriesDto,
                                                          serialize_all_comm_resources_and_categories)
from app.repository.user_repository import UserRepository

user_repository = UserRepository()


class GetCommResourcesByUserAndCategory(object):
    get_comm_resources_by_user_and_category = (
        graphene.List(AllCommResourcesAndCategoriesDto, user_name=graphene.String(), category=graphene.String()))

    def resolve_get_comm_resources_by_user_and_category(self, info, user_name, category):
        query_result = user_repository.get_comm_resources_by_user_and_category(user_name, category)
        return serialize_all_comm_resources_and_categories(query_result)
