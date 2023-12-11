def part1():
    f = open("day11input.txt", "r")

    rows = []
    cols = []

    grid = []

    for i, line in enumerate(f):
        grid.append(line.strip())
        if '#' not in line:
            rows.append(i)

    for c in range(len(grid[0])):
        found = False
        for r in range(len(grid)):
            if grid[r][c] == '#':
                found = True
                break
        if not found:
            cols.append(c)

    poses = []

    for r, line in enumerate(grid):
        for c, cell in enumerate(line):
            if cell == '#':
                poses.append((r, c))

    pairs = [(a, b) for i, a in enumerate(poses) for b in poses[i + 1:]]

    total = 0
    for pair in pairs:
        (r1, c1), (r2, c2) = pair

        cc = 0
        for c in cols:
            if c1 < c < c2 or c2 < c < c1:
                cc += 1
        rr = 0
        for r in rows:
            if r1 < r < r2 or r2 < r < r1:
                rr += 1

        total += abs(r1 - r2) + abs(c1 - c2) + (cc + rr)

    print(total)


def part2():
    f = open("day11input.txt", "r")

    rows = []
    cols = []

    grid = []

    for i, line in enumerate(f):
        grid.append(line.strip())
        if '#' not in line:
            rows.append(i)

    for c in range(len(grid[0])):
        found = False
        for r in range(len(grid)):
            if grid[r][c] == '#':
                found = True
                break
        if not found:
            cols.append(c)

    poses = []

    for r, line in enumerate(grid):
        for c, cell in enumerate(line):
            if cell == '#':
                poses.append((r, c))

    pairs = [(a, b) for i, a in enumerate(poses) for b in poses[i + 1:]]

    total = 0
    for pair in pairs:
        (r1, c1), (r2, c2) = pair

        cc = 0
        for c in cols:
            if c1 < c < c2 or c2 < c < c1:
                cc += 1
        rr = 0
        for r in rows:
            if r1 < r < r2 or r2 < r < r1:
                rr += 1

        total += abs(r1 - r2) + abs(c1 - c2) + (cc + rr) * 999999

    print(total)


part1()
part2()
