with open("input", "r") as file:
    data = [line.strip().split(" -> ") for line in file]

with open("initial_values", "r") as file:
    initial_values = {line.split(": ")[0]: int(line.split(": ")[1]) for line in file}


class Device():
    _instances = {}

    def __new__(cls, op, *inputs):
        name = "-".join(inputs)
        if name in cls._instances:
            return cls._instances[name]
        instance = super(Device, cls).__new__(cls)
        cls._instances[name] = instance
        return instance

    def __init__(self, op, *inputs):
        if not hasattr(self, 'initialized'):
            self.op = self.get_operation(op)
            self.inputs = inputs
            self.initialized = True

    def get_operation(self, op):
        if "AND" in op:
            return lambda a, b: a & b
        elif "XOR" in op:
            return lambda a, b: a ^ b
        elif "OR" in op:
            return lambda a, b: a | b
        else:
            raise ValueError("Invalid operation")

    def run(self):
        values = [Wire.get_instance(input).run() for input in self.inputs]
        if None in values:
            raise ValueError("Not all inputs are initialized")
        return self.op(*values)

    def __str__(self):
        return "-".join(self.inputs)


class Wire():
    _instances = {}

    def __new__(cls, name, value=None, need=None):
        if name in cls._instances:
            return cls._instances[name]
        instance = super(Wire, cls).__new__(cls)
        cls._instances[name] = instance
        return instance

    def __init__(self, name, value=None, need=None):
        if not hasattr(self, 'initialized'):
            self.name = name
            self.value = value
            self.need = need
            self.initialized = True

    @classmethod
    def get_instance(cls, name):
        return cls._instances.get(name)

    def __bool__(self):
        return self.value is not None

    def add_need(self, device):
        self.need = device

    def run(self):
        if self.value is None:
            self.value = self.need.run()
        return self.value

    def update_need(self, need):
        if self.need is None:
            self.need = need
        else:
            raise ValueError("Need already set")

    def __repr__(self):
        return f"Wire({self.name}, {self.value}, {self.need})"


for eq, res in data:
    w1, op, w2 = eq.split(" ")
    Wire(w1, value=initial_values.get(w1, None))
    Wire(w2, value=initial_values.get(w2, None))
    if res not in Wire._instances:
        Wire(res, need=Device(op, w1, w2))
    else:
        Wire._instances[res].add_need(Device(op, w1, w2))

output_wires = []
for n, wire in Wire._instances.items():
    if n.startswith("z"):
        wire.run()
        output_wires.append(wire)

output_wires = sorted(output_wires, key=lambda x: int(x.name[1:]), reverse=True)
number_bin = "".join([str(w.value) for w in output_wires])
number = int(number_bin, 2)
from IPython import embed; embed(header="puzzle.py	l:105")
print(len(number_bin), number)
