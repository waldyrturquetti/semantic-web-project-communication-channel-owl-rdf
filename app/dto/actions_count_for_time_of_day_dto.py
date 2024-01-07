import graphene


class ActionsCountForTimeOfDayDto(graphene.ObjectType):
    class Meta:
        interfaces = (graphene.relay.Node,)

    name = graphene.String()
    time_of_day = graphene.String()
    action_count = graphene.String()


def serialize_action_count_for_time_of_day(results):
    action_count_for_time_of_day = []
    for result in results:
        obj = {
            'name': result['name']['value'],
            'time_of_day': result['timeOfDay']['value'],
            'action_count': result['actionCount']['value']
        }
        action_count_for_time_of_day.append(obj)
    return action_count_for_time_of_day
