import graphene

from app.repository.commchannel_repository import CommChannelRepository
from app.model.commchannel_entity import CommChannel

commchannel_repository = CommChannelRepository()

class GetUserCommChannels(object):
    get_user_commchannels = graphene.List(CommChannel, name=graphene.String())

    def resolve_get_user_commchannels(self, info, name):
        return commchannel_repository.get_user_commchannels(name)