import graphene

class Users(graphene.ObjectType):
    uid = graphene.String()
    gid = graphene.String()
    gid_signed = graphene.String()
    uid_signed = graphene.String()
    username = graphene.String()
    description = graphene.String()
    directory = graphene.String()
    shell = graphene.String()
    uuid = graphene.String()
