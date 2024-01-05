import graphene


class UsersByCommChannelDto(graphene.ObjectType):
    class Meta:
        interfaces = (graphene.relay.Node,)

    name = graphene.String()
    birthday = graphene.String()
    born_country = graphene.String()
    gender = graphene.String()
    height = graphene.String()


def serialize_users_by_comm_channel(results):
    users_by_comm_channel_dto_array = []
    for result in results:
        obj = {
            'name': result['name'],
            'birthday': result['Birthday'],
            'born_country': result['BornCountry'],
            'gender': result['Gender'],
            'height': result['Height'],
        }
        users_by_comm_channel_dto_array.append(obj)
    return users_by_comm_channel_dto_array
