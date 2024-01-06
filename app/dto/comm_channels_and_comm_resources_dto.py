import graphene


class CommChannelsAndCommResourcesDto(graphene.ObjectType):
    class Meta:
        interfaces = (graphene.relay.Node,)

    channel = graphene.String()
    resource = graphene.String()
    weight = graphene.Float()


def serialize_comm_channels_and_comm_resources(results):
    print(results[0]['user'])
    comm_channels_and_comm_resources_dto_array = []


    return comm_channels_and_comm_resources_dto_array
