import graphene


class AllCommResourcesAndCategoriesDto(graphene.ObjectType):
    class Meta:
        interfaces = (graphene.relay.Node,)

    name = graphene.String()
    communication_resource_type = graphene.String()
    communication_channel_category_type = graphene.String()


def serialize_all_comm_resources_and_categories(results):
    all_comm_resources_and_categories = []
    for result in results:
        print(result)
        obj = {
            'name': result['name']['value'],
            'communication_resource_type': result['communication_resource_type']['value'],
            'communication_channel_category_type': result['communication_channel_category_type']['value']
        }
        all_comm_resources_and_categories.append(obj)
    return all_comm_resources_and_categories
