def part1():
    f = open("day10input.txt", 'r')

    grid = []
    cur = None

    for r, line in enumerate(f):
        grid.append(line.strip())
        for c, ch in enumerate(line.strip()):
            if ch == 'S':
                cur = (r, c)


    visited = set()
    order = []

    while cur not in visited:
        visited.add(cur)
        order.append(cur)
        r, c = cur
        ch = grid[r][c]
        if r != 0 and (r - 1, c) not in visited:
            t = grid[r - 1][c]
            if ch == '|' or ch == 'L' or ch == 'J' or ch == 'S':
                if t == '|' or t == 'F' or t == '7':
                    cur = (r - 1, c)
        if r != len(grid) - 1 and (r + 1, c) not in visited:
            t = grid[r + 1][c]
            if ch == '|' or ch == 'F' or ch == '7' or ch == 'S':
                if t == '|' or t == 'L' or t == 'J':
                    cur = (r + 1, c)
        if c != 0 and (r, c - 1) not in visited:
            t = grid[r][c - 1]
            if ch == '-' or ch == '7' or ch == 'J' or ch == 'S':
                if t == '-' or t == 'F' or t == 'L':
                    cur = (r, c - 1)
        if r != len(grid[0]) - 1 and (r, c + 1) not in visited:
            t = grid[r][c + 1]
            if ch == '-' or ch == 'F' or ch == 'L' or ch == 'S':
                if t == '-' or t == '7' or t == 'J':
                    cur = (r, c + 1)

    print(len(order)//2)


def part2():
    f = open("day10input.txt", 'r')

    grid = []
    cur = None

    for r, line in enumerate(f):
        grid.append(line.strip())
        for c, ch in enumerate(line.strip()):
            if ch == 'S':
                cur = (r, c)

    visited = set()
    order = []

    while cur not in visited:
        visited.add(cur)
        order.append(cur)
        r, c = cur
        ch = grid[r][c]
        if r != 0 and (r - 1, c) not in visited:
            t = grid[r - 1][c]
            if ch == '|' or ch == 'L' or ch == 'J' or ch == 'S':
                if t == '|' or t == 'F' or t == '7':
                    cur = (r - 1, c)
        if r != len(grid) - 1 and (r + 1, c) not in visited:
            t = grid[r + 1][c]
            if ch == '|' or ch == 'F' or ch == '7' or ch == 'S':
                if t == '|' or t == 'L' or t == 'J':
                    cur = (r + 1, c)
        if c != 0 and (r, c - 1) not in visited:
            t = grid[r][c - 1]
            if ch == '-' or ch == '7' or ch == 'J' or ch == 'S':
                if t == '-' or t == 'F' or t == 'L':
                    cur = (r, c - 1)
        if r != len(grid[0]) - 1 and (r, c + 1) not in visited:
            t = grid[r][c + 1]
            if ch == '-' or ch == 'F' or ch == 'L' or ch == 'S':
                if t == '-' or t == '7' or t == 'J':
                    cur = (r, c + 1)

    # find the area enclosed by a polygon
    def shoelace_formula(coordinates):
        coordinates.append(coordinates[0])  # close the loop
        n = len(coordinates)
        area = 0.5 * abs(sum(
            coordinates[i][0] * coordinates[(i + 1) % n][1] - coordinates[(i + 1) % n][0] * coordinates[i][1] for i in
            range(n)))
        return int(area)

    # find area that can be covered by len(order) vertices if no points are inside the loop:
    base_area = (len(order) // 2 - 1)

    # every point inside the loop increases this area by 1, so take the difference of areas
    print(shoelace_formula(order) - base_area)


part1()
part2()