import graphene

class OsVersion(graphene.ObjectType):
    name = graphene.String()
    version = graphene.String()
    major = graphene.String()
    minor = graphene.String()
    patch = graphene.String()
    build = graphene.String()
    platform = graphene.String()
    platform_like = graphene.String()
    codename = graphene.String()
