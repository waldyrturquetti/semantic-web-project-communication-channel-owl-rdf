import graphene


class UserContactsRelationshipDto(graphene.ObjectType):
    class Meta:
        interfaces = (graphene.relay.Node,)

    relation_source = graphene.String()
    relationship = graphene.String()
    relation_end = graphene.String()


def serialize_user_contacts_relationship(results):
    user_contacts_dto_array = []
    print(results)
    for result in results:
        obj = {
            'relation_source': result['r'][0]['name'],
            'relationship': result['r'][1],
            'relation_end': result['r'][2]['name'],
        }
        user_contacts_dto_array.append(obj)

    return user_contacts_dto_array
