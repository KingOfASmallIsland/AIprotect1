import numpy as np

f = open("p1_graph.txt")
a = np.empty([100, 2], dtype=int)
b = np.empty([985, 3], dtype=int)
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
        h = nums[1]
    if nums[0] == 'D':
        p = nums[1]
    k = k + 1

path = np.empty([100, 100], dtype=int)
sp = np.empty([100], dtype=int)
spt = np.empty([100], dtype=bool)
for i in range(0, 100):
    sp[i] = 100000
    spt[i] = False

sp[0] = 0
spt[0] = True
vertex = 0
path[0][0] = 0

x = 100
while x != 0:
    for i in range (len(b)):
        if b[i][0] == vertex:
            if b[i][2] + sp[vertex] < sp[b[i][1]]:
                sp[b[i][1]] = b[i][2] + sp[vertex]


        if b[i][1] == vertex:
            if b[i][2] + sp[vertex] < sp[b[i][0]]:
                sp[b[i][0]] = b[i][2] + sp[vertex]

    sv = 100000
    for i in range(len(spt)):
        if not spt[i]:
            if sp[i] < sv:
                vertex = i
    spt[vertex] = True

    x = x-1

print(sp[99])











