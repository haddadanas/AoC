import awkward as ak
import numpy as np

# read the file
with open("input", "r") as file:
    file = file.readlines()
file = [line.split() for line in file]
file = ak.Array([[int(x) for x in line] for line in file])

# part 1
flat = ak.flatten(file)
diff = np.diff(flat, append=0)
diff = ak.unflatten(diff, ak.num(file))
diff = diff[:, :-1]

direction_mask = ak.all(diff < 0, axis=1) | ak.all(diff > 0, axis=1)
distance_mask = ak.all(abs(diff) >= 1, axis=1) & ak.all(abs(diff) <= 3, axis=1)
mask = direction_mask & distance_mask

print(f"the number of valid passwords is {ak.sum(mask)}")

# part 2
unsafe = file[~mask]
# unsafe_diff = diff[~mask]
# num_allowed = ak.num(unsafe) - 2
# unsafe_direction_mask = (ak.sum(unsafe_diff < 0, axis=1) >= num_allowed) | (ak.sum(unsafe_diff > 0, axis=1) >= num_allowed)

# unsafe = unsafe[unsafe_direction_mask]
# unsafe_diff = unsafe_diff[unsafe_direction_mask]

# sel_mask = (unsafe_diff < 0) | (unsafe_diff > 0)
# unsafe_diff = unsafe_diff[sel_mask]

# from IPython import embed; embed(header="Debugger")
# unsafe_distance_mask = (abs(unsafe_diff) >= 1) & (abs(unsafe_diff) <= 3)
# accept_mask = ak.sum(~unsafe_distance_mask, axis=1) < 2

# unsafe = unsafe[accept_mask]
# unsafe_distance_mask = unsafe_distance_mask[accept_mask]
# outlier = unsafe_diff[~unsafe_distance_mask]
# unsafe_diff = unsafe_diff[unsafe_distance_mask]

def check_if_safe(array):
    arr_diff = np.diff(array)
    direction_mask = np.all(arr_diff < 0) | np.all(arr_diff > 0)
    distance_mask = np.all(abs(arr_diff) >= 1) & np.all(abs(arr_diff) <= 3)
    mask = direction_mask & distance_mask
    return mask

n_unsafe = 0
for array in unsafe:
    for i in range(len(array)):
        red_array = np.delete(array, i)
        if check_if_safe(red_array):
            n_unsafe += 1
            break

print(f"the number of safe passwords is {ak.sum(mask) + n_unsafe}")
