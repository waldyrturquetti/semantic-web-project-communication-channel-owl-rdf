import graphene

class User(graphene.ObjectType):
    class Meta:
        interfaces = (graphene.relay.Node,)

    # id = graphene.ID()
    name = graphene.String()
    birthday = graphene.String()
    born_country = graphene.String()
    gender = graphene.String()
    height = graphene.String()

def serialize_user(user):
    return {
        "name": user["name"],
        "birthday": user["Birthday"],
        "born_country": user["BornCountry"],
        "gender": user["Gender"],
        "height": user["Height"],
        }
