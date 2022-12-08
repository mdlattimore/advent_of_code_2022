# Nailed this one (after hours of avoiding work). Haven't yet figured out Part 2.

import numpy as np
from day8_data import data


a = [int(w) for w in data if w.isnumeric()]
trees = np.array(a).reshape(99, 99)


visible = []  # coordinates of visible interior trees
for idx, row in enumerate(trees[1:-1]):

    for i, v in enumerate(row[1:-1]):
        target = int(row[i+1])
        left = all(row[:i+1] < target)
        right = all(row[i+2:] < target)
        if np.all(left):
            visible.append((idx+1, i+1))
        elif np.all(right):
            visible.append((idx+1, i+1))

trees_col = np.swapaxes(trees, 0, 1)

for idx, row in enumerate(trees_col[1:-1]):
    for i, v in enumerate(row[1:-1]):
        target = int(row[i+1])
        left = all(row[:i+1] < target)
        right = all(row[i+2:] < target)
        if np.all(left):
            visible.append((i+1, idx+1))  # flipped index references since we swapped axes
        elif np.all(right):
            visible.append((i+1, idx+1))

# print(visible)
# Part 1 Answer
print(len(set(visible)) + 392)  # 392 is the number of trees on the perimeter which are always visible


