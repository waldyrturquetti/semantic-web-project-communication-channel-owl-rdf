import graphene


class ActionsByCommChannelDto(graphene.ObjectType):
    class Meta:
        interfaces = (graphene.relay.Node,)

    type = graphene.String()


def serialize_action_by_comm_channel(results):
    action_by_comm_channel_dto_array = []
    print(results)
    for result in results:
        obj = {
            'type': result['a']['type'],
        }
        action_by_comm_channel_dto_array.append(obj)
    return action_by_comm_channel_dto_array
