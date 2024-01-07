import graphene

from app.dto.greater_action_count_per_category_dto import (GreaterActionCountPerCategoryDto,
                                                          serialize_greater_action_count_per_category)
from app.repository.user_repository import UserRepository

user_repository = UserRepository()


class GetGreaterActionCountPerCategoryByUser(object):
    get_greater_action_count_per_category_by_user = (
        graphene.List(GreaterActionCountPerCategoryDto, user_name=graphene.String()))

    def resolve_get_greater_action_count_per_category_by_user(self, info, user_name):
        query_result = user_repository.get_greater_action_count_per_category_by_user(user_name)
        return serialize_greater_action_count_per_category(query_result)
