import graphene

class EtcHosts(graphene.ObjectType):
    address = graphene.String()
    hostnames = graphene.String()
