import graphene


class ActionsCountForActionCategoryDto(graphene.ObjectType):
    class Meta:
        interfaces = (graphene.relay.Node,)

    name = graphene.String()
    action_category = graphene.String()
    action_category_count = graphene.String()


def serialize_action_count_for_action_category(results):
    action_count_for_action_category = []
    for result in results:
        obj = {
            'name': result['name']['value'],
            'action_category': result['actionCategory']['value'],
            'action_category_count': result['actionCategoryCount']['value']
        }
        action_count_for_action_category.append(obj)
    return action_count_for_action_category
