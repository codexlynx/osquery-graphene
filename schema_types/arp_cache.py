import graphene

class ArpCache(graphene.ObjectType):
    address = graphene.String()
    mac = graphene.String()
    interface = graphene.String()
    permanent = graphene.String()
