import graphene

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
