import graphene
import osquery

query = osquery.OSQuery()

class Cpuid(graphene.ObjectType):
    feature = graphene.String()
    value = graphene.String()
    output_register = graphene.String()
    output_bit = graphene.String()
    input_eax = graphene.String()

class EtcProtocols(graphene.ObjectType):
    name = graphene.String()
    number = graphene.String()
    alias = graphene.String()
    comment = graphene.String()

class Query(graphene.ObjectType):
    cpuid = graphene.List(Cpuid)

    def resolve_cpuid(self, args, context, info):
        for item in query.run('select * from cpuid'):
            yield Cpuid(
                    feature=item['feature'],
                    value=item['value'],
                    output_register=item['output_register'],
                    output_bit=item['output_bit'],
                    input_eax=item['input_eax']
            )

    etc_protocols = graphene.List(EtcProtocols)

    def resolve_etc_protocols(self, args, context, info):
        for item in query.run('select * from etc_protocols'):
            yield EtcProtocols(
                    name=item['name'],
                    number=item['number'],
                    alias=item['alias'],
                    comment=item['comment']
            )

schema = graphene.Schema(query=Query)
