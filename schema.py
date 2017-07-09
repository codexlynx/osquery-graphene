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

class EtcServices(graphene.ObjectType):
    name = graphene.String()
    port = graphene.String()
    protocol = graphene.String()
    aliases = graphene.String()
    comment = graphene.String()

class InterfaceAddresses(graphene.ObjectType):
    interface = graphene.String()
    address = graphene.String()
    mask = graphene.String()
    broadcast = graphene.String()
    point_to_point = graphene.String()
    #type = graphene.String()

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

    etc_services = graphene.List(EtcServices)

    def resolve_etc_services(self, args, context, info):
        for item in query.run('select * from etc_services'):
            yield EtcServices(
                    name=item['name'],
                    port=item['port'],
                    protocol=item['protocol'],
                    aliases=item['aliases'],
                    comment=item['comment']
            )

    interface_addresses = graphene.List(InterfaceAddresses)

    def resolve_interface_addresses(self, args, context, info):
        for item in query.run('select * from interface_addresses'):
            yield InterfaceAddresses(
                    interface=item['interface'],
                    address=item['address'],
                    mask=item['mask'],
                    broadcast=item['broadcast'],
                    point_to_point=item['point_to_point']
                    #type=item['type']
            )

schema = graphene.Schema(query=Query)
