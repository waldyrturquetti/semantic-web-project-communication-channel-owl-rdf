import graphene

from app.model.user_entity import User
from app.repository.commchannel_repository import CommChannelRepository

comm_channel_repository = CommChannelRepository()


class GetUsersByCommChannel(object):
    get_users_by_comm_channel = (
        graphene.List(User, cc_type=graphene.String()))

    def resolve_get_users_by_comm_channel(self, info, cc_type):
        return comm_channel_repository.get_users_by_comm_channel(cc_type)