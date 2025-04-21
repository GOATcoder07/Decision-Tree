import numpy as np
import pandas as pd

rng = np.random.RandomState(1)
X = np.sort(200 * rng.rand(100, 1) - 100, axis=0)
y = np.array([np.pi * np.sin(X).ravel(), np.pi * np.cos(X).ravel()]).T
y[::5, :] += 0.5 - rng.rand(20, 2)

def mean_squared_error(data):
    if len(data) == 0:
        return 0
    mean = np.mean(data)
    return np.mean((data - mean) ** 2)

def best_split(x, y):
    sorted_idx = np.argsort(x)
    x_sorted = x[sorted_idx]
    y_sorted = y[sorted_idx]
    min_error = np.inf
    split_value = None

    for i in range(1, len(x_sorted)):
        if x_sorted[i] == x_sorted[i-1]:
            continue
        current_split = (x_sorted[i] + x_sorted[i-1]) / 2
        left_mask = x_sorted <= current_split
        left_error = mean_squared_error(y_sorted[left_mask])
        right_error = mean_squared_error(y_sorted[left_mask])
        total_error = left_error + right_error
        if total_error < min_error:
            min_error = total_error
            split_value = current_split

    return split_value, min_error