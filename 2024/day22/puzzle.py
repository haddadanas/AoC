import numpy as np

data = np.loadtxt('input', dtype=int)


def prune(number: np.ndarray):
    return number % 16777216


def mix(number: np.ndarray, value: int):
    return number ^ value


def calculate_next_secret(secret: np.ndarray):
    result = np.zeros_like(secret)
    # Step 1
    result = prune(mix(secret, secret * 64))

    # Step 2
    result = prune(mix(result, np.astype(np.floor(result / 32), int)))

    # Step 3
    result = prune(mix(result, result * 2048))

    return result


result = np.zeros((len(data), 2001), dtype=int)
result[:, 0] = data
for i in range(2000):
    result[:, i + 1] = calculate_next_secret(result[:, i])

print(result[:, -1].sum())

# get the ones digit
price = result % 10
change = np.diff(price, axis=1)

change1 = change.reshape((len(data), -1, 4))
change2 = change[:, 1:1997].reshape((len(data), -1, 4))
change3 = change[:, 2:1998].reshape((len(data), -1, 4))
change4 = change[:, 3:1999].reshape((len(data), -1, 4))


from IPython import embed; embed(header="puzzle.py	l:11")
