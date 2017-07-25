import graphene

class ProcessOpenSockets(graphene.ObjectType):
    pid = graphene.String()
    fd = graphene.String()
    socket = graphene.String()
    family = graphene.String()
    protocol = graphene.String()
    local_address = graphene.String()
    remote_address = graphene.String()
