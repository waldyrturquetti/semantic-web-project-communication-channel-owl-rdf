import graphene

class PhoneNumber(graphene.ObjectType):
    class Meta:
        interfaces = (graphene.relay.Node,)

    # id = graphene.ID()
    country_id = graphene.String()
    number = graphene.String()
