class Router:
    "This is a simulation class of router's work"
    def __init__(self, brand, model, hostname):
        self.brand = brand
        self.model = model
        self.hostname = hostname
        self.interfaces = {}

    def add_interface(self, inf):
        self.interfaces[inf] = {'ip': 'unassigned', 'status': 'shutdown', 'connect': ['none', 'none']}

    def connect_to(self, inf1, router2, inf2):
        self.interfaces[inf1]['connect'] = [router2.hostname, inf2]
        router2.interfaces[inf2]['connect'] = [self.hostname, inf1]
    
    def show_interfaces(self):
        txt = "Show Interfaces of %s\n%s has %d interfaces\n"%(self.hostname, self.hostname, len(self.interfaces))
        for inf in self.interfaces:
            txt += "%s IP-Address: %s \"%s\"\n"%(inf, self.interfaces[inf]['ip'], self.interfaces[inf]['status'])
        return txt

    def show_info(self):
        txt = "Brand: %s\nModel: %s\nHostname: %s\n"%(self.brand, self.model, self.hostname)
        return txt

    def show_cdp(self):
        txt = ""
        for inf in self.interfaces:
            if self.interfaces[inf]['connect'] != ['none', 'none']:
                txt += "%s interface %s connect to %s on interface %s\n"%(self.hostname, inf, self.interfaces[inf]['connect'][0], self.interfaces[inf]['connect'][1])    
        return txt

    def add_ip(self, inf, ip):
        self.interfaces[inf]['ip'] = ip

    def change_status(self, inf, status):
        self.interfaces[inf]['status'] = status