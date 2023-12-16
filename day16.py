def part1():
    f = open("day16input.txt", 'r')

    grid = []

    for line in f:
        grid.append(line.strip())

    visited = [[False] * len(grid[0]) for _ in range(len(grid))]
    done = []

    queue = [(0, -1, 'E')]

    while queue:
        r, c, d = queue.pop()
        if c != -1:
            if (r, c, d) in done:
                continue
            done.append((r, c, d))
            visited[r][c] = True
        if d == 'E':
            if c + 1 >= len(grid[0]):
                continue
            if grid[r][c + 1] == '\\':
                queue.append((r, c + 1, 'S'))
            elif grid[r][c + 1] == '/':
                queue.append((r, c + 1, 'N'))
            elif grid[r][c + 1] == '|':
                queue.append((r, c + 1, 'N'))
                queue.append((r, c + 1, 'S'))
            else:
                queue.append((r, c + 1, 'E'))
        if d == 'W':
            if c - 1 < 0:
                continue
            if grid[r][c - 1] == '\\':
                queue.append((r, c - 1, 'N'))
            elif grid[r][c - 1] == '/':
                queue.append((r, c - 1, 'S'))
            elif grid[r][c - 1] == '|':
                queue.append((r, c - 1, 'N'))
                queue.append((r, c - 1, 'S'))
            else:
                queue.append((r, c - 1, 'W'))
        if d == 'S':
            if r + 1 >= len(grid):
                continue
            if grid[r + 1][c] == '\\':
                queue.append((r + 1, c, 'E'))
            elif grid[r + 1][c] == '/':
                queue.append((r + 1, c, 'W'))
            elif grid[r + 1][c] == '-':
                queue.append((r + 1, c, 'W'))
                queue.append((r + 1, c, 'E'))
            else:
                queue.append((r + 1, c, 'S'))
        if d == 'N':
            if r - 1 < 0:
                continue
            if grid[r - 1][c] == '\\':
                queue.append((r - 1, c, 'W'))
            elif grid[r - 1][c] == '/':
                queue.append((r - 1, c, 'E'))
            elif grid[r - 1][c] == '-':
                queue.append((r - 1, c, 'W'))
                queue.append((r - 1, c, 'E'))
            else:
                queue.append((r - 1, c, 'N'))

    total = 0
    for line in visited:
        total += sum(line)
    print(total)


def part2():
    f = open("day16input.txt", 'r')

    grid = []

    for line in f:
        grid.append(line.strip())

    starts = []
    for r in range(len(grid)):
        starts.append((r, -1, 'E'))
        starts.append((r, len(grid[0]), 'W'))
    for c in range(len(grid[0])):
        starts.append((-1, c, 'S'))
        starts.append((len(grid), c, 'N'))

    best = 0

    for start in starts:
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        done = []
        queue = [start]
        while queue:
            r, c, d = queue.pop()
            if 0 <= c < len(grid[0]) and 0 <= r < len(grid):
                if (r, c, d) in done:
                    continue
                done.append((r, c, d))
                visited[r][c] = True
            if d == 'E':
                if c + 1 >= len(grid[0]):
                    continue
                if grid[r][c + 1] == '\\':
                    queue.append((r, c + 1, 'S'))
                elif grid[r][c + 1] == '/':
                    queue.append((r, c + 1, 'N'))
                elif grid[r][c + 1] == '|':
                    queue.append((r, c + 1, 'N'))
                    queue.append((r, c + 1, 'S'))
                else:
                    queue.append((r, c + 1, 'E'))
            if d == 'W':
                if c - 1 < 0:
                    continue
                if grid[r][c - 1] == '\\':
                    queue.append((r, c - 1, 'N'))
                elif grid[r][c - 1] == '/':
                    queue.append((r, c - 1, 'S'))
                elif grid[r][c - 1] == '|':
                    queue.append((r, c - 1, 'N'))
                    queue.append((r, c - 1, 'S'))
                else:
                    queue.append((r, c - 1, 'W'))
            if d == 'S':
                if r + 1 >= len(grid):
                    continue
                if grid[r + 1][c] == '\\':
                    queue.append((r + 1, c, 'E'))
                elif grid[r + 1][c] == '/':
                    queue.append((r + 1, c, 'W'))
                elif grid[r + 1][c] == '-':
                    queue.append((r + 1, c, 'W'))
                    queue.append((r + 1, c, 'E'))
                else:
                    queue.append((r + 1, c, 'S'))
            if d == 'N':
                if r - 1 < 0:
                    continue
                if grid[r - 1][c] == '\\':
                    queue.append((r - 1, c, 'W'))
                elif grid[r - 1][c] == '/':
                    queue.append((r - 1, c, 'E'))
                elif grid[r - 1][c] == '-':
                    queue.append((r - 1, c, 'W'))
                    queue.append((r - 1, c, 'E'))
                else:
                    queue.append((r - 1, c, 'N'))

        total = 0
        for line in visited:
            total += sum(line)

        best = max(best, total)

    print(best)


part1()
part2()
