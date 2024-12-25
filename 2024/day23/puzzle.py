with open("input") as f:
    data = [line.split("-") for line in f.read().strip().split("\n")]


class HashSet(set):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __hash__(self):
        _hash = 0
        for i in self:
            _hash += hash(i)
        return _hash


class Port:
    _instances = {}

    def __new__(cls, name):
        if name in cls._instances:
            return cls._instances[name]
        instance = super(Port, cls).__new__(cls)
        cls._instances[name] = instance
        return instance

    def __init__(self, name):
        if not hasattr(self, 'initialized'):
            self.name = name
            self.connections = set()
            self.initialized = True

    @classmethod
    def get_instance(cls, name):
        return cls._instances.get(name)

    def __hash__(self):
        return hash(self.name)

    def add(self, port):
        self.connections.add(port)

    def starts_with_t(self):
        return self.name.startswith("t")

    def has_port(self, port):
        return port in self.connections

    def __len__(self):
        return len(self.connections)

    def __lt__(self, other):
        return self.name < other.name


# part 1
relevant_ports = set()
for port1, port2 in data:
    port1 = Port(port1)
    port2 = Port(port2)
    port1.add(port2)
    port2.add(port1)
    if port1.starts_with_t():
        relevant_ports.add(port1)
    if port2.starts_with_t():
        relevant_ports.add(port2)


connected_ports = set()
for port in relevant_ports:
    for p2 in port.connections:
        for p3 in p2.connections:
            if p3.has_port(port):
                connected_ports.add(HashSet([port.name, p2.name, p3.name]))

print(len(connected_ports))


# part 2
def find_largest_clique(ports):
    longest_connections = set()
    all_ports = list(ports.values())

    def backtrack(start, current_clique):
        nonlocal longest_connections
        if len(current_clique) > len(longest_connections):
            longest_connections = current_clique.copy()
        for i in range(start, len(all_ports)):
            port = all_ports[i]
            if all(p in port.connections for p in current_clique):
                current_clique.add(port)
                backtrack(i + 1, current_clique)
                current_clique.remove(port)

    backtrack(0, set())
    return longest_connections


largest_clique = find_largest_clique(Port._instances)
password = ",".join(sorted(port.name for port in largest_clique))
print(password)