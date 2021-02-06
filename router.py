class Router:
    "define router attributes"

    def __init__(self, brand, model, hostname, interfaces):
        self.brand = brand
        self.model = model
        self.hostname = hostname
        self.interfaces = {}

    def add_interface(self, intf):
        self.interfaces[intf] = {'IP-Address' : 'unassigned', 'Status' : 'administratively down', 'Protocol' : 'down'}