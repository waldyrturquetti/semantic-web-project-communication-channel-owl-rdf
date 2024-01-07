import graphene

from app.dto.actions_count_for_time_of_day_dto import (ActionsCountForTimeOfDayDto,
                                                          serialize_action_count_for_time_of_day)
from app.repository.user_repository import UserRepository

user_repository = UserRepository()


class GetActionsCountInEachTimeOfDayByUser(object):
    get_actions_count_in_each_time_of_day_by_user = (
        graphene.List(ActionsCountForTimeOfDayDto, user_name=graphene.String()))

    def resolve_get_actions_count_in_each_time_of_day_by_user(self, info, user_name):
        query_result = user_repository.get_actions_count_in_each_time_of_day_by_user(user_name)
        return serialize_action_count_for_time_of_day(query_result)
