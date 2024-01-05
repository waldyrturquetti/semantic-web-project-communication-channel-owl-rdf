import graphene

class User(graphene.ObjectType):
    class Meta:
        interfaces = (graphene.relay.Node,)

    # id = graphene.ID()
    type = graphene.String()
    name = graphene.String()
    birthday = graphene.String()
    born_country = graphene.String()
    gender = graphene.String()
    height = graphene.String()