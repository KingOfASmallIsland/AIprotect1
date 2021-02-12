from dijkstar import Graph, find_path
import numpy as np
f = open("p1_graph.txt")
p = open("p1_graph.txt")
alen = 0
blen = 0
for data in p.readlines():
    data = data.strip("\n")
    nums = data.split(',')

    if len(nums) == 2 and nums[0] != 'S' and nums[0] != 'D' and nums[0] != "# Vertex ID":
        alen = alen + 1
    if len(nums) == 3 and nums[0] != "# From":
        blen = blen + 1

a = np.empty([alen, 2], dtype=int)
b = np.empty([blen, 3], dtype=int)
c = np.empty([1, 2], dtype=int)
d = np.empty([1, 2], dtype=int)
i = 0
k = 0
x = 0


for data in f.readlines():
    data = data.strip("\n")
    nums = data.split(',')

    if len(nums) == 2 and nums[0] != 'S' and nums[0] != 'D' and nums[0] != "# Vertex ID":
        for j in range(len(nums)):
            a[i][j] = nums[j]
        i = i + 1

    if len(nums) == 3 and nums[0] != "# From":
        for j in range(len(nums)):
            b[x][j] = nums[j]
        x = x + 1

    if nums[0] == 'S':
        c[0][0] = nums[1]
    if nums[0] == 'D':
        d[0][0] = nums[1]
    k = k + 1

graph = Graph()
for i in range (len(b)):
    graph.add_edge(b[i][0], b[i][1], b[i][2])

print(find_path(graph, c[0][0], d[0][0]))







