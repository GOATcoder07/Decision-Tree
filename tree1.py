import numpy as np
import pandas as pd
rng = np.random.default_rng()
df = pd.read_fwf('hitters.txt')
years = df['Years'].values
runs = df["Runs"].values
runs = np.sort(rng.normal(size = N))
def sum_squared_error(data):
    d = data - np.mean(data)
    return np.sum(d*d)
n = len(years)
for i in range(1, n): 
    leftSum = np.sum(runs[:i])
    rightSum = np.sum(runs[i:])
    total = leftSum + rightSum
    error = (leftSum ** 2) + (rightSum **2)
np.argmin(total)
def bestSplit(x, y):
    minError = float('inf')
    sorted = np.argsort(x)
    xSort = x[sorted]
    ySort = y[sorted]
    length = len(ySort)
    for i in range(1,n):
        left = ySort[:i]
        right = ySort[i:]
        leftSum = sum_squared_error(left)
        rightSum = sum_squared_error(right)
        total = leftSum + rightSum
        if total < minError:
            minError = total
    return minError


    