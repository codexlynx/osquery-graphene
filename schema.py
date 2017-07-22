import graphene
import osquery
import utils

query = osquery.OSQuery()

class ArpCache(graphene.ObjectType):
    address = graphene.String()
    mac = graphene.String()
    interface = graphene.String()
    permanent = graphene.String()

class Cpuid(graphene.ObjectType):
    feature = graphene.String()
    value = graphene.String()
    output_register = graphene.String()
    output_bit = graphene.String()
    input_eax = graphene.String()

class EtcHosts(graphene.ObjectType):
    address = graphene.String()
    hostnames = graphene.String()

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

class Hash(graphene.ObjectType):
    path = graphene.String()
    directory = graphene.String()
    md5 = graphene.String()
    sha1 = graphene.String()
    sha256 = graphene.String()

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

class ListeningPorts(graphene.ObjectType):
    pid = graphene.String()
    port = graphene.String()
    protocol = graphene.String()
    family = graphene.String()
    address = graphene.String()

class LoggedInUsers(graphene.ObjectType):
    type = graphene.String()
    user = graphene.String()
    tty = graphene.String()
    host = graphene.String()
    time = graphene.String()
    pid = graphene.String()

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

class PlatformInfo(graphene.ObjectType):
    vendor = graphene.String()
    version = graphene.String()
    date = graphene.String()
    revision = graphene.String()
    address = graphene.String()
    size = graphene.String()
    volume_size = graphene.String()
    extra = graphene.String()

class ProcessOpenSockets(graphene.ObjectType):
    pid = graphene.String()
    fd = graphene.String()
    socket = graphene.String()
    family = graphene.String()
    protocol = graphene.String()
    local_address = graphene.String()
    remote_address = graphene.String()

class Processes(graphene.ObjectType):
    pid = graphene.String()
    name = graphene.String()
    path = graphene.String()
    cmdline = graphene.String()
    state = graphene.String()
    cwd = graphene.String()
    root = graphene.String()
    uid = graphene.String()
    gid = graphene.String()
    euid = graphene.String()
    egid = graphene.String()
    suid = graphene.String()
    sgid = graphene.String()
    on_disk = graphene.String()
    wired_size = graphene.String()
    resident_size = graphene.String()
    total_size = graphene.String()
    user_time = graphene.String()
    system_time = graphene.String()
    start_time = graphene.String()
    parent = graphene.String()
    pgroup = graphene.String()
    threads = graphene.String()
    nice = graphene.String()

class Routes(graphene.ObjectType):
    destination = graphene.String()
    netmask = graphene.String()
    gateway = graphene.String()
    source = graphene.String()
    flags = graphene.String()
    interface = graphene.String()
    mtu = graphene.String()
    metric = graphene.String()
    type = graphene.String()

class StartupItems(graphene.ObjectType):
    name = graphene.String()
    path = graphene.String()
    args = graphene.String()
    type = graphene.String()
    source = graphene.String()
    status = graphene.String()
    username = graphene.String()

class SystemInfo(graphene.ObjectType):
    hostname = graphene.String()
    uuid = graphene.String()
    cpu_type = graphene.String()
    cpu_subtype = graphene.String()
    cpu_brand = graphene.String()
    cpu_physical_cores = graphene.String()
    cpu_logical_cores = graphene.String()
    physical_memory = graphene.String()
    hardware_vendor = graphene.String()
    hardware_model = graphene.String()
    hardware_version = graphene.String()
    hardware_serial = graphene.String()
    computer_name = graphene.String()
    #local_hostname = graphene.String()

class Uptime(graphene.ObjectType):
    days = graphene.String()
    hours = graphene.String()
    minutes = graphene.String()
    seconds = graphene.String()
    total_seconds = graphene.String()

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

'''
class About(graphene.ObjectType):
    name = graphene.String()
'''

class Query(graphene.ObjectType):

    arp_cache = graphene.List(ArpCache)

    def resolve_arp_cache(self, args, context, info):
        for item in query.run('select ^from arp_cache'):
            yield ArpCache(
                    address=item['address'],
                    mac=item['mac'],
                    interface=item['interface'],
                    permanent=item['permanent']
            )

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

    etc_hosts = graphene.List(EtcHosts)

    def resolve_etc_hosts(self, args, context, info):
        for item in query.run('select * from etc_hosts'):
            yield EtcHosts(
                    address=item['address'],
                    hostnames=item['hostnames']
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

    hash = graphene.List(Hash, directory=graphene.String(),
                               path=graphene.String()
    )

    def resolve_hash(self, args, context, info):
        if args.get('directory'): where = 'directory = \\"%s\\"' % utils.sanitize(args.get('directory'))
        if args.get('path'): where = 'path = \\"%s\\"' % utils.sanitize(args.get('path'))
        for item in query.run('select * from hash where %s' % where):
            yield Hash(
                    path=item['path'],
                    directory=item['directory'],
                    md5=item['md5'],
                    sha1=item['sha1'],
                    sha256=item['sha256']
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

    listening_ports = graphene.List(ListeningPorts)

    def resolve_listening_ports(self, args, context, info):
        for item in query.run('select * from listening_ports'):
            yield ListeningPorts(
                    pid=item['pid'],
                    port=item['port'],
                    protocol=item['protocol'],
                    family=item['family'],
                    address=item['address']
            )

    logged_in_users = graphene.List(LoggedInUsers)

    def resolve_logged_in_users(self, args, context, info):
        for item in query.run('select * from logged_in_users'):
            yield LoggedInUsers(
                    type=item['type'],
                    user=item['user'],
                    tty=item['tty'],
                    host=item['host'],
                    time=item['time'],
                    pid=item['pid']
            )

    os_version = graphene.List(OsVersion)

    def resolve_os_version(self, args, context, info):
        for item in query.run('select * from os_version'):
            yield OsVersion(
                    name=item['name'],
                    version=item['version'],
                    major=item['major'],
                    minor=item['minor'],
                    patch=item['patch'],
                    build=item['build'],
                    platform=item['platform'],
                    platform_like=item['platform_like'],
                    codename=item['codename']
            )

    platform_info = graphene.List(PlatformInfo)

    def resolve_platform_info(self, args, context, info):
        for item in query.run('select * from platform_info'):
            yield PlatformInfo(
                    vendor=item['vendor'],
                    version=item['version'],
                    date=date['date'],
                    revision=item['revision'],
                    address=item['address'],
                    size=item['size'],
                    volume_size=item['volume_size'],
                    extra=item['extra']
            )

    process_open_sockets = graphene.List(ProcessOpenSockets)

    def resolve_process_open_sockets(self, args, context, info):
        for item in query.run('select * from process_open_sockets'):
            yield ProcessOpenSockets(
                    pid=item['pid'],
                    fd=item['fd'],
                    socket=item['socket'],
                    family=item['family'],
                    protocol=item['protocol'],
                    local_address=item['local_address'],
                    remote_address=remote_address['remote_address']
            )

    processes = graphene.List(Processes)

    def resolve_processes(self, args, context, info):
        for item in query.run('select * from processes'):
            yield Processes(
                    pid=item['pid'],
                    name=item['name'],
                    path=item['path'],
                    cmdline=item['cmdline'],
                    state=item['state'],
                    cwd=item['cwd'],
                    root=item['root'],
                    uid=item['uid'],
                    gid=item['gid'],
                    euid=item['euid'],
                    egid=item['egid'],
                    suid=item['suid'],
                    sgid=item['sgid'],
                    on_disk=item['on_disk'],
                    wired_size=item['wired_size'],
                    resident_size=item['resident_size'],
                    total_size=item['total_size'],
                    user_time=item['user_time'],
                    system_time=item['system_time'],
                    start_time=item['start_time'],
                    parent=item['parent'],
                    pgroup=item['pgroup'],
                    threads=item['threads'],
                    nice=item['nice']
            )

    routes = graphene.List(Routes)

    def resolve_routes(self, args, context, info):
        for item in query.run('select * from routes'):
            yield Routes(
                    destination=item['destination'],
                    netmask=item['netmask'],
                    gateway=item['gateway'],
                    source=item['source'],
                    flags=item['flags'],
                    interface=item['interface'],
                    mtu=item['mtu'],
                    metric=item['metric'],
                    type=item['type']
            )

    startup_items = graphene.List(StartupItems)

    def resolve_startup_items(self, args, context, info):
        for item in query.run('select * from startup_items'):
            yield StartupItems(
                    name=item['name'],
                    path=item['path'],
                    args=item['args'],
                    type=item['type'],
                    source=item['source'],
                    status=item['status'],
                    username=item['username']
            )

    system_info = graphene.List(SystemInfo)

    def resolve_system_info(self, args, context, info):
        for item in query.run('select * from system_info'):
            yield SystemInfo(
                    hostname=item['hostname'],
                    uuid=item['uuid'],
                    cpu_type=item['cpu_type'],
                    cpu_subtype=item['cpu_subtype'],
                    cpu_brand=item['cpu_brand'],
                    cpu_physical_cores=item['cpu_physical_cores'],
                    cpu_logical_cores=item['cpu_logical_cores'],
                    physical_memory=item['physical_memory'],
                    hardware_vendor=item['hardware_vendor'],
                    hardware_model=item['hardware_model'],
                    hardware_version=item['hardware_version'],
                    hardware_serial=item['hardware_serial'],
                    computer_name=item['computer_name']#,
                    #local_hostname=item['local_hostname']
            )

    uptime = graphene.List(Uptime)

    def resolve_uptime(self, args, context, info):
        for item in query.run('select * from uptime'):
            yield Uptime(
                    days=item['days'],
                    hours=item['hours'],
                    minutes=item['minutes'],
                    seconds=item['seconds'],
                    total_seconds=item['total_seconds']
            )

    users = graphene.List(Users)

    def resolve_users(self, args, context, info):
        for item in query.run('select * from users'):
            yield Users(
                    uid=item['uid'],
                    gid=item['gid'],
                    gid_signed=item['gid_signed'],
                    uid_signed=item['uid_signed'],
                    username=item['username'],
                    description=item['description'],
                    directory=item['directory'],
                    shell=item['shell'],
                    uuid=item['uuid']
            )

    test = graphene.String()

    def resolve_test(self, args, context, info):
        return 'test'

schema = graphene.Schema(query=Query)
