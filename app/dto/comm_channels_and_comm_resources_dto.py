import graphene


class CommChannelsAndCommResourcesDto(graphene.ObjectType):
    class Meta:
        interfaces = (graphene.relay.Node,)

    channel = graphene.String()
    resource = graphene.String()
    resource_type = graphene.String()
    weight = graphene.Float()


def serialize_comm_channels_and_comm_resources(results):
    comm_channels_and_comm_resources_dto_array = []
    for result in results:
        obj = {
            'channel': result['communication_channel_type']['value'],
            'resource': result['communication_resource_value']['value'],
            'resource_type': result['communication_resource_type']['value'],
            'weight': result['preference_weight']['value'],
        }
        comm_channels_and_comm_resources_dto_array.append(obj)

    return comm_channels_and_comm_resources_dto_array
