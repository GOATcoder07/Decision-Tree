import numpy as np

def sum_squared_error(data):
    if len(data) == 0:
        return 0
    mean = np.mean(data)
    return np.sum((data - mean) ** 2)

def best_split(x, y):
    sorted_idx = np.argsort(x)
    x_sorted = x[sorted_idx]
    y_sorted = y[sorted_idx]
    min_error = float('inf')
    split_value = None

    for i in range(1, len(x_sorted)):
        if x_sorted[i] == x_sorted[i-1]:
            continue
        current_split = (x_sorted[i] + x_sorted[i-1]) / 2
        left_mask = x_sorted <= current_split
        left_error = sum_squared_error(y_sorted[left_mask])
        right_error = sum_squared_error(y_sorted[~left_mask])
        total_error = left_error + right_error
        if total_error < min_error:
            min_error = total_error
            split_value = current_split

    return split_value, min_error
