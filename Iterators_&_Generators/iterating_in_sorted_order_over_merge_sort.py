import heapq

a = [1, 2, 4, 7]
b = [3, 5, 6, 8]

for c in heapq.merge(a, b):
    print(c)