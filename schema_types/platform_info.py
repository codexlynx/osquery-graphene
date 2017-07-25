import graphene

class PlatformInfo(graphene.ObjectType):
    vendor = graphene.String()
    version = graphene.String()
    date = graphene.String()
    revision = graphene.String()
    address = graphene.String()
    size = graphene.String()
    volume_size = graphene.String()
    extra = graphene.String()
