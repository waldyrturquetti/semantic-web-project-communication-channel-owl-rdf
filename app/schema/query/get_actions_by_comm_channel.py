import graphene

from app.dto.actions_by_comm_channel_dto import ActionsByCommChannelDto
from app.repository.commchannel_repository import CommChannelRepository

comm_channel_repository = CommChannelRepository()


class GetActionByCommChannel(object):
    get_actions_by_comm_channel = (
        graphene.List(ActionsByCommChannelDto, cc_type=graphene.String()))

    def resolve_get_actions_by_comm_channel(self, info, cc_type):
        return comm_channel_repository.get_actions_by_comm_channel(cc_type)