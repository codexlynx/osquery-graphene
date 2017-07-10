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

class InterfaceDetails(graphene.ObjectType):
    interface = graphene.String()
    mac = graphene.String()
    type = graphene.String()
    mtu = graphene.String()
    metric = graphene.String()
    flags = graphene.String()
    ipackets = graphene.String()
    opackets = graphene.String()
    ibytes = graphene.String()
    obytes = graphene.String()
    ierrors = graphene.String()
    oerrors = graphene.String()
    idrops = graphene.String()
    odrops = graphene.String()
    last_change = graphene.String()
    description = graphene.String()
    manufacturer = graphene.String()
    connection_id = graphene.String()
    connection_status = graphene.String()
    enabled = graphene.String()
    physical_adapter = graphene.String()
    speed = graphene.String()
    dhcp_enabled = graphene.String()
    dhcp_lease_expires = graphene.String()
    dhcp_lease_obtained = graphene.String()
    dhcp_server = graphene.String()
    dns_domain = graphene.String()
    dns_domain_suffix_search_order = graphene.String()
    dns_host_name = graphene.String()
    dns_server_search_order = graphene.String()

class KernelInfo(graphene.ObjectType):
    version = graphene.String()
    arguments = graphene.String()
    path = graphene.String()
    device = graphene.String()

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

    interface_details = graphene.List(InterfaceDetails)

    def resolve_interface_details(self, args, context, info):
        for item in query.run('select * from interface_details'):
            yield InterfaceDetails(
                    interface=item['interface'],
                    mac=item['mac'],
                    type=item['type'],
                    mtu =item['mtu'],
                    metric=item['metric'],
                    #flags=item['flags'],
                    ipackets=item['ipackets'],
                    opackets=item['opackets'],
                    ibytes=item['ibytes'],
                    obytes=item['obytes'],
                    ierrors=item['ierrors'],
                    oerrors=item['oerrors'],
                    idrops=item['idrops'],
                    odrops=item['odrops'],
                    last_change=item['last_change'],
                    description=item['description'],
                    manufacturer=item['manufacturer'],
                    connection_id=item['connection_id'],
                    connection_status=item['connection_status'],
                    enabled=item['enabled'],
                    physical_adapter=item['physical_adapter'],
                    speed=item['speed'],
                    dhcp_enabled=item['dhcp_enabled'],
                    dhcp_lease_expires=item['dhcp_lease_expires'],
                    dhcp_lease_obtained=item['dhcp_lease_obtained'],
                    dhcp_server=item['dhcp_server'],
                    dns_domain=item['dns_domain'],
                    dns_domain_suffix_search_order=item['dns_domain_suffix_search_order'],
                    dns_host_name=item['dns_host_name'],
                    dns_server_search_order=item['dns_server_search_order']
            )

    kernel_info = graphene.List(KernelInfo)

    def resolve_kernel_info(self, args, context, info):
        for item in query.run('select * from kernel_info'):
            yield KernelInfo(
                    version=item['version'],
                    arguments=item['arguments'],
                    path=item['path'],
                    device=item['device']
            )


schema = graphene.Schema(query=Query)
