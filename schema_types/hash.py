import graphene

class Hash(graphene.ObjectType):
    path = graphene.String()
    directory = graphene.String()
    md5 = graphene.String()
    sha1 = graphene.String()
    sha256 = graphene.String()
