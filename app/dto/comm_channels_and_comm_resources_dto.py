import graphene


class CommChannelsAndCommResourcesDto(graphene.ObjectType):
    class Meta:
        interfaces = (graphene.relay.Node,)

    channel = graphene.String()
    resource = graphene.String()
    weight = graphene.Float()


def serialize_comm_channels_and_comm_resources(results):
    comm_channels_and_comm_resources_dto_array = []
    for result in results:
        obj = None
        if result['a'].get('country_id') is not None:
            obj = {
                'channel': result['cc']['type'],
                'resource': result['a']['country_id'] + result['a']['number'],
                'weight': result['PROPERTIES(h)']['preference_weight'],
            }
        if result['a'].get('email') is not None:
            obj = {
                'channel': result['cc']['type'],
                'resource': result['a']['email'],
                'weight': result['PROPERTIES(h)']['preference_weight'],
            }
        if result['a'].get('app_name') is not None:
            obj = {
                'channel': result['cc']['type'],
                'resource': result['a']['app_name'],
                'weight': result['PROPERTIES(h)']['preference_weight'],
            }
        comm_channels_and_comm_resources_dto_array.append(obj)

    return comm_channels_and_comm_resources_dto_array
