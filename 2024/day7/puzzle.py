from operator import mul, add
import awkward as ak
import numpy as np

with open("input", "r") as file:
    data = ak.Array([line.split(":") for line in file.readlines()])

values = ak.Array([int(x) for x in data[:, 0]])
equations = ak.Array([[int(x) for x in eq.split()] for eq in data[:, 1]])


def solve(equation, value, length):
    ops = ak.cartesian([["+", "*"] for _ in range(length - 1)], axis=0)
    op_map = {"+": add, "*": mul}
    solve = ak.zeros_like(value) == 1
    for operation in ops:
        operation = operation.tolist()
        op = op_map[operation[0]]
        res = op(equation[:, 0], equation[:, 1])
        for i in range(1, length - 1):
            op = op_map[operation[i]]
            res = op(res, equation[:, i + 1])
        solve = solve | (res == value)

    return ak.sum(value[solve])


# eq_num = ak.num(equations)
# eq_sum = 0
# for n in range(ak.min(eq_num), ak.max(eq_num) + 1):
#     mask = eq_num == n
#     eq_sum += solve(equations[mask], values[mask], n)


# print(eq_sum)


# part 2
def solve_with_concatenate(equation, value, length):
    result = 0
    ops = ak.cartesian([["+", "*"] for _ in range(length - 1)], axis=0)
    op_map = {"+": add, "*": mul}
    solve = ak.zeros_like(value) == 1
    for operation in ops:
        operation = operation.tolist()
        op = op_map[operation[0]]
        res = op(equation[:, 0], equation[:, 1])
        for i in range(1, length - 1):
            op = op_map[operation[i]]
            res = op(res, equation[:, i + 1])
        solve = solve | (res == value)

    result = ak.sum(value[solve])
    equation = equation[~solve]
    value = value[~solve]
    solve = ak.zeros_like(value) == 1
    ops = ak.cartesian([["+", "*", "|"] for _ in range(length - 1)], axis=0)
    op_map = {"+": add, "*": mul, "|": concat_nums}
    for operation in ops:
        operation = operation.tolist()
        op = op_map[operation[0]]
        res = op(equation[:, 0], equation[:, 1])
        for i in range(1, length - 1):
            op = op_map[operation[i]]
            res = op(res, equation[:, i + 1])
        solve = solve | (res == value)
    result += ak.sum(value[solve])
    return result


def concat_nums(a, b):
    a = np.astype(a.to_numpy(), str)
    b = np.array(b.to_numpy(), str)
    return ak.Array(np.astype(a + b, int))


eq_num = ak.num(equations)
eq_sum = 0
for n in range(ak.min(eq_num), ak.max(eq_num) + 1):
    print(f"Working on equations with {n} elements")
    mask = eq_num == n
    eq_sum += solve_with_concatenate(equations[mask], values[mask], n)
print(eq_sum)
