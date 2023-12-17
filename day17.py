import heapq

DIRECTIONS = [(-1, 0, 'up'), (1, 0, 'down'), (0, -1, 'left'), (0, 1, 'right')]
OPPOSITE = {'up': 'down', 'left': 'right', 'down': 'up', 'right': 'left'}
INF = 1e20

def part1():
    def astar(grid):
        height, width = len(grid), len(grid[0])
        start, end = (0, 0), (height - 1, width - 1)
        pr_queue = [(heuristic(start, end), (0, start, ""))]
        visited = set()
        g_score = {}

        while pr_queue:
            _, (dist, (y, x), last_dir) = heapq.heappop(pr_queue)
            if (y, x) == end:
                print(dist)
                return
            if ((y, x), last_dir) in visited:
                continue
            visited.add(((y, x), last_dir))
            for ay, ax, direction in DIRECTIONS:
                if last_dir == direction or last_dir == OPPOSITE[direction]:
                    continue
                d = dist
                for i in range(1, 4):
                    ny = y + ay * i
                    nx = x + ax * i
                    if ny < 0 or nx < 0 or ny >= height or nx >= width:
                        continue
                    d += grid[ny][nx]
                    if g_score.get(((ny, nx), direction), INF) <= d:
                        continue
                    g_score[((ny, nx), direction)] = d
                    heapq.heappush(pr_queue, (d + heuristic((ny, nx), end), (d, (ny, nx), direction)))

    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    f = open("day17input.txt", 'r')
    grid = [list(map(int, list(line))) for line in f.read().split('\n')]
    astar(grid)


def part2():
    def astar(grid):
        height, width = len(grid), len(grid[0])
        start, end = (0, 0), (height - 1, width - 1)
        pr_queue = [(0 + heuristic(start, end), (0, start, ""))]
        visited = set()
        g_score = {}

        while pr_queue:
            _, (dist, (y, x), last_dir) = heapq.heappop(pr_queue)
            if (y, x) == end:
                print(dist)
                return
            if ((y, x), last_dir) in visited:
                continue
            visited.add(((y, x), last_dir))
            for ay, ax, direction in DIRECTIONS:
                if last_dir == direction or last_dir == OPPOSITE[direction]:
                    continue
                d = dist
                for i in range(1, 11):
                    ny = y + ay * i
                    nx = x + ax * i
                    if ny < 0 or nx < 0 or ny >= height or nx >= width:
                        continue
                    d += grid[ny][nx]
                    if i < 4:
                        continue
                    if g_score.get(((ny, nx), direction), INF) <= d:
                        continue
                    g_score[((ny, nx), direction)] = d
                    heapq.heappush(pr_queue, (d + heuristic((ny, nx), end), (d, (ny, nx), direction)))

    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    f = open("day17input.txt", 'r')
    grid = [list(map(int, list(line))) for line in f.read().split('\n')]
    astar(grid)


part1()
part2()
