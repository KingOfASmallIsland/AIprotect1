import numpy as np
from heapq import heappush,heappop

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
apath = np.zeros([len(a), len(a)], dtype=int)

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
            apath[int(nums[0])][int(nums[1])] = int(nums[2])
            apath[int(nums[1])][int(nums[0])] = int(nums[2])
        x = x + 1

    if nums[0] == 'S':
        c[0][0] = nums[1]
    if nums[0] == 'D':
        d[0][0] = nums[1]
    k = k + 1

def hscore(neighbor, goal):
    x1 = int(neighbor / 10 - goal / 10) * 1000

    y1 = int(neighbor % 10 - goal % 10) * 1000
    # print("1: ", neighbor, "2:  ", goal,"  x:",x1,"  Y:", y1, "  sqrt:", np.sqrt(abs(x1)*abs(x1) + abs(y1)*abs(y1))*10)
    return np.sqrt(abs(x1) * abs(x1) + abs(y1) * abs(y1))

def g_score(a, b):
    return apath[a][b]


def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path


start = c[0][0]
goal = d[0][0]
close_set = set()
came_from = {}
gscore = {start: 0}
fscore = {start: hscore(start, goal)}

openSet = []
heappush(openSet, (fscore[start], start))

while len(openSet) != 0:
    current = heappop(openSet)[1]

    if current == goal:
        print(reconstruct_path(came_from, current))

    close_set.add(current)
    for i in range(len(apath[start])):
        neighbor = i
        if apath[current][neighbor] == 0:
            continue
        if neighbor in close_set:
            continue

        gscoretotal = gscore[current] + g_score(current, neighbor)

        if neighbor not in [j[1] for j in openSet]:
            heappush(openSet, (fscore.get(neighbor, np.inf), neighbor))
        elif gscoretotal >= gscore.get(neighbor, np.inf):
            continue

        came_from[neighbor] = current
        gscore[neighbor] = gscoretotal
        fscore[neighbor] = gscoretotal + hscore(neighbor, goal)



