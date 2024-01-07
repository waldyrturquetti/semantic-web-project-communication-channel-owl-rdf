import graphene


class GreaterActionCountPerCategoryDto(graphene.ObjectType):
    class Meta:
        interfaces = (graphene.relay.Node,)

    name = graphene.String()
    action_category = graphene.String()
    action_category_count = graphene.String()


def serialize_greater_action_count_per_category(results):
    greater_action_count_per_category = []
    for result in results:
        print(result)
        obj = {
            'name': result['name']['value'],
            'action_category': result['actionCategory']['value'],
            'action_category_count': result['actionCategoryCount']['value']
        }
        greater_action_count_per_category.append(obj)
    return greater_action_count_per_category
