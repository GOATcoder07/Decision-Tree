import numpy as np
import pandas as pd

# Initialize random number generator
rng = np.random.default_rng()
N = 100  # Size of the data
runs = np.sort(rng.normal(size = N))

# Function to calculate sum of squared errors
def sum_squared_error(data):
    d = data - np.mean(data)
    return np.sum(d * d)

# Initialize arrays to store left, right, total errors
left = np.zeros(N)
right = np.zeros(N)
total = np.zeros(N)

# Loop through possible splits
for i in range(1, N): 
    left[i] = sum_squared_error(runs[:i])  # Sum squared error for left side
    right[i] = sum_squared_error(runs[i:])  # Sum squared error for right side
    total[i] = left[i] + right[i]  # Total error is the sum of left and right errors

# Find the split with the minimum total error (excluding split 0)
min_index = np.argmin(total[1:]) + 1  # Add 1 to index since total starts at 1

# Print the result
print(f"Optimal split index: {min_index}")
print(f"Left sum squared error: {left[min_index]}")
print(f"Right sum squared error: {right[min_index]}")
