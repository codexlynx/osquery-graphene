import graphene

class Welcome(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()

class Query(graphene.ObjectType):
    welcome = graphene.Field(Welcome)

    def resolve_welcome(self, args, context, info):
        return Welcome(id=1, name='Antonio')

schema = graphene.Schema(query=Query)
