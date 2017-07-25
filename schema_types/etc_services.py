import graphene

class EtcServices(graphene.ObjectType):
    name = graphene.String()
    port = graphene.String()
    protocol = graphene.String()
    aliases = graphene.String()
    comment = graphene.String()
