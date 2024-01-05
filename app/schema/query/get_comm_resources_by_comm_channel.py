import graphene

from app.dto.comm_resources_by_comm_channel_dto import CommResourcesByCommChannelDto
from app.repository.commchannel_repository import CommChannelRepository

comm_channel_repository = CommChannelRepository()


class GetCommResourcesByCommChannel(object):
    get_comm_resources_by_comm_channel = (
        graphene.List(CommResourcesByCommChannelDto, cc_type=graphene.String()))

    def resolve_get_comm_resources_by_comm_channel(self, info, cc_type):
        return comm_channel_repository.get_comm_resources_by_comm_channel(cc_type)