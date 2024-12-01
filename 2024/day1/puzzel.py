import numpy as np

file = np.loadtxt('input', dtype=int)

x1 = file[:, 0]
x2 = file[:, 1]

# part 1
x1_sorted = np.sort(x1)
x2_sorted = np.sort(x2)

result1 = np.sum(np.abs(x1_sorted - x2_sorted))
print(f"the sum of distances is {result1}")

# part 2
unique_x1, ind = np.unique(x1, return_inverse=True)
mapping_dict = {k: v for k, v in zip(*np.unique(x2, return_counts=True))}

counts = np.array([mapping_dict.get(x, 0) for x in unique_x1])[ind]

result2 = np.sum(x1 * counts)
print(f"the sum of unique counts is {result2}")
