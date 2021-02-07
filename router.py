class Router:
    "define router attributes"
    def __init__(self, brand, model, hostname):
        self.brand = ""
        self.model = ""
        self.hostname = ""
        self.interfaces = {}

    def add_interface(self, inf):
        "Add anoter interfaces to router"
        self.interfaces[inf] = {'IP-Address' : 'unassigned', 'Status' : 'administratively down', 'Protocol' : 'down'}