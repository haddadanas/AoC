import sys
from copy import deepcopy
from matplotlib.pylab import f
import numpy as np

sys.path.append("C:\\Users\\famil\\Documents\\Sonstiges\\AoC\\2025\\")

from aoc_utils import read_input, validate_test


class Circuit:
    def __init__(self):
        self.junctions: set[Junction] = set()

    def __hash__(self) -> int:
        return hash(tuple(sorted(j.id for j in self.junctions)))

    def __repr__(self) -> str:
        return f"Circuit with {len(self.junctions)} junctions"

    def add_junction(self, junction: "Junction") -> None:
        self.junctions.add(junction)

    def merge(self, other: "Circuit") -> None:
        self.junctions |= other.junctions

    def size(self) -> int:
        return len(self.junctions)


class Junction:
    def __init__(self, coords: list[str], id: int):
        self.xyz = np.array(list(map(int, coords)))
        self.id = id
        self.circuit_id = id
        # self.connections: set[Junction] = {self}

    def distance(self, other: "Junction") -> float:
        return np.linalg.norm(self.xyz - other.xyz).item()

    # def connect(self, other: "Junction") -> None:
    #     connections = self.connections | other.connections
    #     for junction in connections:
    #         junction.connections = connections

    def __repr__(self) -> str:
        return f"Junction {self.id}"

    def __hash__(self) -> int:
        return hash(self.id) + hash(tuple(self.xyz))


class Junctions:
    def __init__(self) -> None:
        self.circuits: dict[int, Circuit] = {}
        self.junctions: dict[int, Junction] = {}

    def add_junction(self, junction: Junction) -> None:
        self.junctions[junction.id] = junction
        circuit = Circuit()
        circuit.add_junction(junction)
        self.circuits[junction.circuit_id] = circuit

    def get_junction(self, id: int) -> Junction:
        return self.junctions[id]

    def connect(self, id1: int, id2: int) -> None:
        junction1 = self.junctions[id1]
        junction2 = self.junctions[id2]
        circuit1 = self.circuits[junction1.circuit_id]
        circuit2 = self.circuits[junction2.circuit_id]
        if circuit1 == circuit2:
            return
        circuit1.merge(circuit2)
        self.circuits.pop(junction2.circuit_id)
        for j in circuit2.junctions:
            j.circuit_id = junction1.circuit_id


def connect_junctions(junctions: Junctions, max_iter: int = -1):
    juncs = sorted(junctions.junctions.values(), key=lambda j: j.id)
    distances = np.array([list(map(j.distance, juncs)) for j in juncs])
    distances[distances == 0] = 100000
    for _ in range(max_iter):
        i, j = np.unravel_index(np.argmin(distances), distances.shape)
        junctions.connect(int(i), int(j))
        distances[i, j] = 100000
        distances[j, i] = 100000
    return distances


def connect_all_junctions(junctions: Junctions, distances: np.ndarray | None = None):
    if distances is None:
        juncs = sorted(junctions.junctions.values(), key=lambda j: j.id)
        distances = np.array([list(map(j.distance, juncs)) for j in juncs])
    distances[distances == 0] = 100000
    while len(junctions.circuits) != 1:
        i, j = np.unravel_index(np.argmin(distances), distances.shape)
        junctions.connect(int(i), int(j))
        distances[i, j] = 100000
        distances[j, i] = 100000
    return list(map(junctions.get_junction, (int(i), int(j))))


if __name__ == "__main__":
    test_junctions = Junctions()
    input_junctions = Junctions()

    for i, line in enumerate(read_input("test.txt", "\n")):
        test_junctions.add_junction(Junction(line.split(","), i))

    for i, line in enumerate(read_input("input.txt", "\n")):
        input_junctions.add_junction(Junction(line.split(","), i))

    test_distances = connect_junctions(test_junctions, 10)
    input_distances = connect_junctions(input_junctions, 1000)

    validate_test(np.unique(list(map(lambda x: x.size(), test_junctions.circuits.values())))[-3:].prod(), 40)
    print("Part 1:", np.unique(list(map(lambda x: x.size(), input_junctions.circuits.values())))[-3:].prod())

    test_i, test_j = connect_all_junctions(test_junctions, test_distances)
    input_i, input_j = connect_all_junctions(input_junctions, input_distances)

    validate_test(test_i.xyz[0] * test_j.xyz[0], 25272)
    print("Part 2:", input_i.xyz[0] * input_j.xyz[0])