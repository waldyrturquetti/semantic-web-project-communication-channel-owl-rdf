import graphene

from app.dto.comm_channels_and_comm_resources_dto import CommChannelsAndCommResourcesDto
from app.repository.commchannel_repository import CommChannelRepository

comm_channel_repository = CommChannelRepository()


class GetCommChannelsAndCommResourcesByUser(object):
    get_comm_channels_and_comm_resources_by_user = (
        graphene.List(CommChannelsAndCommResourcesDto, user_name=graphene.String()))

    def resolve_get_comm_channels_and_comm_resources_by_user(self, info, user_name):
        return comm_channel_repository.get_comm_channels_and_comm_resources_by_user(user_name)
