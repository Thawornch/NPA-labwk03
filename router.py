class Router:
    "define router attributes"
    def __init__(self, brand, model, hostname):
        self.brand = brand
        self.model = model
        self.hostname = hostname
        self.interfaces = {}

    def add_interface(self, inf):
        "Add anoter interfaces to router"
        self.interfaces[inf] = {'IP-Address' : 'unassigned', 'Status' : 'administratively down', 'Protocol' : 'down'}
    
    def show_interfaces(self):
        "show all interfaces of router"
        result = "Show interfaces of %s\n%s has %d interfaces\n" %(self.hostname, self.hostname, len(self.interfaces))
        for inf in self.interfaces:
            result += "%s\n" %inf
        return result