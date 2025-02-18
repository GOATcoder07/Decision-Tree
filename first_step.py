import numpy as np

rng = np.random.default_rng()
N = 100
x = rng.normal(size = N)

def sum_squared_error(data):
    d = data - np.mean(data)
    return np.sum(d * d)

total = np.zeros(N)
for i in range(N):
    total[i] += sum_squared_error(x[:i])
    total[i] += sum_squared_error(x[i:])

np.argmin(total)
