# Numpy arrays
import numpy as np

# Python Lists
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]

ax = np.array(x)
ay = np.array(y)

# print(ax*2)
# print(ax + 10)
# print(ax + ay)
# print(ax * ay)


grid = np.zeros(shape=(100, 10), dtype=float)
grid += 10
print(np.sin(grid))
print(grid)

