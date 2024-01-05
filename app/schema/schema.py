import graphene

from app.schema.mutation.create_user import CreateUser

from app.schema.query.get_user import GetUser
from app.schema.query.get_user_commchannels import GetUserCommChannels
from app.schema.query.get_comm_channels_and_comm_resources_by_user import GetCommChannelsAndCommResourcesByUser
from app.schema.query.get_usercontact_relationships import GetUserContactsRelationship
from app.schema.query.get_actions_by_comm_channel import GetActionByCommChannel
from app.schema.query.get_comm_resources_by_comm_channel import GetCommResourcesByCommChannel
from app.schema.query.get_the_best_comm_channels_and_comm_resources_by_user import GetTheBestCommChannelsAndCommResourcesByUser
from app.schema.query.get_users_by_comm_channel import GetUsersByCommChannel


class Query(GetUser,
            GetUserCommChannels,
            GetCommChannelsAndCommResourcesByUser,
            GetUserContactsRelationship,
            GetActionByCommChannel,
            GetCommResourcesByCommChannel,
            GetTheBestCommChannelsAndCommResourcesByUser,
            GetUsersByCommChannel,
            graphene.ObjectType):
    pass


class Mutations(CreateUser, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutations)
