import graphene

from app.schema.mutation.create_user import CreateUser

from app.schema.query.get_the_best_comm_channels_and_comm_resources_by_user import GetTheBestCommChannelsAndCommResourcesByUser
from app.schema.query.get_all_comm_channels_and_comm_resources_by_user import GetAllCommChannelsAndCommResourcesByUser
from app.schema.query.get_actions_count_in_each_time_of_day_by_user import GetActionsCountInEachTimeOfDayByUser
from app.schema.query.get_count_for_each_action_category_by_user import GetActionsCountForActionCategoryByUser
from app.schema.query.get_the_greater_action_count_per_category_by_user import GetGreaterActionCountPerCategoryByUser

class Query(
    GetTheBestCommChannelsAndCommResourcesByUser,
    GetAllCommChannelsAndCommResourcesByUser,
    GetActionsCountInEachTimeOfDayByUser,
    GetActionsCountForActionCategoryByUser,
    GetGreaterActionCountPerCategoryByUser,
    graphene.ObjectType):
    pass


class Mutations(CreateUser, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutations)
