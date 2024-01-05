import graphene

from app.model.user_entity import User


class CreateUser(graphene.Mutation):
    class Input:
        name = graphene.String(required=True)
        birthday = graphene.String(required=True)
        born_country = graphene.String(required=True)
        gender = graphene.String(required=True)
        height = graphene.String(required=False)

    user = graphene.Field(User)

    def mutate(self, info, name, birthday, born_country, gender, height):
        user = User(name=name, birthday=birthday, born_country=born_country, gender=gender, height=height)
        return CreateUser(
            user=user,
        )
