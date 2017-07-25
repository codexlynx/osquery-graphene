import graphene

class LoggedInUsers(graphene.ObjectType):
    type = graphene.String()
    user = graphene.String()
    tty = graphene.String()
    host = graphene.String()
    time = graphene.String()
    pid = graphene.String()
