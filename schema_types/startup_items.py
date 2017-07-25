import graphene

class StartupItems(graphene.ObjectType):
    name = graphene.String()
    path = graphene.String()
    args = graphene.String()
    type = graphene.String()
    source = graphene.String()
    status = graphene.String()
    username = graphene.String()
