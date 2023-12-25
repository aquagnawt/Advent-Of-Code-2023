import random
import sys
sys.setrecursionlimit(10**6)

f = open("day25input.txt", 'r')

adj = dict()
components = set()

for line in f:
    cur, neighbours = line.split(": ")
    if cur not in adj:
        adj[cur] = set()
    components.add(cur)
    for n in neighbours.split():
        if n not in adj:
            adj[n] = set()
        adj[cur].add(n)
        adj[n].add(cur)
        components.add(n)

def get_path(start, end):
    queue = [start]
    visited = set()
    parent = {}
    while queue:
        cur = queue.pop(0)
        for n in adj[cur]:
            if n in visited:
                continue
            visited.add(n)
            queue.append(n)
            parent[n] = cur
            if n == end:
                break

    path = [end]
    cur = end
    while cur != start:
        cur = parent[cur]
        path.append(cur)
    return path

def get_size(cur, visited):
    visited.add(cur)
    for n in adj[cur]:
        if n in visited:
            continue
        get_size(n, visited)
    return len(visited)

edge_count = dict()
components = list(components)
while True:
    c1 = random.choice(components)
    c2 = random.choice(components)
    if c1 == c2 or c1 in adj[c2] or c2 in adj[c1]:
        continue
    path = get_path(c1, c2)
    for i in range(len(path)-1):
        edge = tuple(sorted([path[i], path[i+1]]))
        if edge not in edge_count:
            edge_count[edge] = 0
        edge_count[edge] += 1
    removing = sorted(edge_count.keys(), key=lambda x: edge_count[x], reverse=True)[:3]
    for a, b in removing:
        adj[a].remove(b)
        adj[b].remove(a)
    if get_size(c1, set()) != len(components):
        print(get_size(c1, set()) * get_size(c2, set()))
        break
    for a, b in removing:
        adj[a].add(b)
        adj[b].add(a)



