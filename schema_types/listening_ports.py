import graphene

class ListeningPorts(graphene.ObjectType):
    pid = graphene.String()
    port = graphene.String()
    protocol = graphene.String()
    family = graphene.String()
    address = graphene.String()
