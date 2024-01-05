import graphene

from app.schema.mutation.create_user import CreateUser

from app.schema.query.get_the_best_comm_channels_and_comm_resources_by_user import \
    GetTheBestCommChannelsAndCommResourcesByUser


class Query(
    GetTheBestCommChannelsAndCommResourcesByUser,
    graphene.ObjectType):
    pass


class Mutations(CreateUser, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutations)
