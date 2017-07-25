import graphene

class KernelInfo(graphene.ObjectType):
    version = graphene.String()
    arguments = graphene.String()
    path = graphene.String()
    device = graphene.String()
