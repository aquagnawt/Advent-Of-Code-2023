import sys
sys.setrecursionlimit(10**6)

def part1():
    f = open("day23input.txt", 'r')
    grid = f.read().split("\n")

    D = {(0, 1): '>', (0, -1): '<', (1, 0): 'v', (-1, 0): '^'}

    visited = set()
    def dfs(cur, depth):
        if cur in visited:
            return 0
        if cur == (len(grid) - 1, len(grid[0]) - 2):
            return depth
        visited.add(cur)
        r, c = cur
        max_depth = depth
        for a, b in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            rr, cc = r + a, c + b
            if not (0 <= rr < len(grid) and 0 <= cc < len(grid[0])):
                continue
            if not (grid[rr][cc] == '.' or grid[rr][cc] == D[(a, b)]):
                continue
            max_depth = max(max_depth, dfs((rr, cc), depth + 1))
        visited.remove(cur)
        return max_depth

    print(dfs((0, 1), 0))


def part2():
    f = open("day23input.txt", 'r')
    grid = f.read().split("\n")

    visited = set()
    adj = {}

    def count_neighbours(cur):
        r, c = cur
        n = 0
        for a, b in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            rr, cc = r + a, c + b
            if not (0 <= rr < len(grid) and 0 <= cc < len(grid[0])):
                continue
            if grid[rr][cc] != '#':
                n += 1
        return n

    def fill(cur, parent, depth):
        if cur in visited:
            return
        visited.add(cur)
        r, c = cur
        for a, b in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            rr, cc = r + a, c + b
            if not (0 <= rr < len(grid) and 0 <= cc < len(grid[0])):
                continue
            if grid[rr][cc] == '#':
                continue
            if count_neighbours((rr, cc)) > 2 or (rr, cc) in ((0, 1), (len(grid) - 1, len(grid[0]) - 2)):
                if (rr, cc) == parent:
                    continue
                adj[parent][(rr, cc)] = depth
            else:
                fill((rr, cc), parent, depth + 1)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != '#' and (
                    count_neighbours((i, j)) > 2 or (i, j) in ((0, 1), (len(grid) - 1, len(grid[0]) - 2))):
                visited.clear()
                adj[(i, j)] = {}
                fill((i, j), (i, j), 1)

    visited.clear()

    def dfs(cur, depth):
        global m
        if cur in visited:
            return 0
        if cur == (len(grid) - 1, len(grid[0]) - 2):
            return depth
        visited.add(cur)
        max_depth = 0
        for neighbour in adj[cur]:
            max_depth = max(max_depth, dfs(neighbour, depth + adj[cur][neighbour]))
        visited.remove(cur)
        return max_depth

    print(dfs((0, 1), 0))


# part1()
part2()