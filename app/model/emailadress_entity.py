import graphene

class EmailAddress(graphene.ObjectType):
    class Meta:
        interfaces = (graphene.relay.Node,)

    # id = graphene.ID()
    email = graphene.String()
