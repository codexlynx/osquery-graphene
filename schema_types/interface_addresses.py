import graphene

class InterfaceAddresses(graphene.ObjectType):
    interface = graphene.String()
    address = graphene.String()
    mask = graphene.String()
    broadcast = graphene.String()
    point_to_point = graphene.String()
    #type = graphene.String()
