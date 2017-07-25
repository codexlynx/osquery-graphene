import graphene

class Uptime(graphene.ObjectType):
    days = graphene.String()
    hours = graphene.String()
    minutes = graphene.String()
    seconds = graphene.String()
    total_seconds = graphene.String()
