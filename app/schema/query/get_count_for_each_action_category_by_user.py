import graphene

from app.dto.action_count_for_each_action_category_dto import (ActionsCountForActionCategoryDto,
                                                          serialize_action_count_for_action_category)
from app.repository.user_repository import UserRepository

user_repository = UserRepository()


class GetActionsCountForActionCategoryByUser(object):
    get_actions_count_for_each_action_category_by_user = (
        graphene.List(ActionsCountForActionCategoryDto, user_name=graphene.String()))

    def resolve_get_actions_count_for_each_action_category_by_user(self, info, user_name):
        query_result = user_repository.get_actions_count_for_each_action_category_by_user(user_name)
        return serialize_action_count_for_action_category(query_result)
