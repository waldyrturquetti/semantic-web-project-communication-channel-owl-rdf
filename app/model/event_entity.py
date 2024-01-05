import graphene

class Event(graphene.ObjectType):
    class Meta:
        interfaces = (graphene.relay.Node,)

    # id = graphene.ID()
    context = graphene.String()
    enddate = graphene.String()
    nature = graphene.String()
    place = graphene.String()
    startdate = graphene.String()
    title = graphene.String()
    type = graphene.String()