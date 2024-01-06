import graphene

from app.dto.comm_channels_and_comm_resources_dto import (CommChannelsAndCommResourcesDto,
                                                          serialize_comm_channels_and_comm_resources)
from app.repository.commchannel_repository import CommChannelRepository

comm_channel_repository = CommChannelRepository()


class GetTheBestCommChannelsAndCommResourcesByUser(object):
    get_the_best_comm_channels_and_comm_resources_by_user = (
        graphene.List(CommChannelsAndCommResourcesDto, user_name=graphene.String()))

    def resolve_get_the_best_comm_channels_and_comm_resources_by_user(self, info, user_name):
        query_result = comm_channel_repository.get_the_best_comm_channels_and_comm_resources_by_user(user_name)
        return serialize_comm_channels_and_comm_resources(query_result)
