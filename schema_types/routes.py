import graphene

class Routes(graphene.ObjectType):
    destination = graphene.String()
    netmask = graphene.String()
    gateway = graphene.String()
    source = graphene.String()
    flags = graphene.String()
    interface = graphene.String()
    mtu = graphene.String()
    metric = graphene.String()
    type = graphene.String()
