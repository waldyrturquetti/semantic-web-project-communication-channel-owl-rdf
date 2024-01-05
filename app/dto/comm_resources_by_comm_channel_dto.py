import graphene


class CommResourcesByCommChannelDto(graphene.ObjectType):
    class Meta:
        interfaces = (graphene.relay.Node,)

    comm_resource = graphene.String()


def serialize_comm_resources_by_comm_channel(results):
    comm_resources_by_comm_channel = []
    print(results)
    for result in results:
        display_comm_resources = ""
        for item in reversed(result['A']):
            display_comm_resources += result['A'][item]
        obj = {
            'comm_resource': display_comm_resources,
        }
        comm_resources_by_comm_channel.append(obj)

    return comm_resources_by_comm_channel
