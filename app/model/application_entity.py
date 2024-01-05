import graphene

class User(graphene.ObjectType):
    class Meta:
        interfaces = (graphene.relay.Node,)

    # id = graphene.ID()
    app_name = graphene.String()