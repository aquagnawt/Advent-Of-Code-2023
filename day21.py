def part1():
    f = open("day21input.txt", 'r')
    grid = f.read().split("\n")

    start = None
    for i, line in enumerate(grid):
        if 'S' in line:
            start = (i, line.index('S'))
            break

    queue = [(start, 0)]
    visited = set()
    total = 0
    while queue:
        cur, n = queue.pop(0)
        if cur in visited:
            continue
        if n > 64:
            continue
        visited.add(cur)
        r, c = cur
        if n % 2 == 0:
            total += 1
        for a, b in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            rr, cc = r + a, c + b
            if not (0 <= rr < len(grid) and 0 <= cc < len(grid[0])):
                continue
            if grid[rr][cc] == '#':
                continue
            queue.append(((rr, cc), n+1))

    print(total)


def part2():
    f = open("day21input.txt", 'r')
    grid = f.read().split("\n")

    start = None
    for i, line in enumerate(grid):
        if 'S' in line:
            start = (i, line.index('S'))

    queue = [(start, 0)]
    visited = set()
    evens_square = 0  # number of plots that can be reached by an even number of steps in the original grid.
    evens_diamond = 0  # number of plots that can be reached by an even number of steps, after 65 steps from the origin.
    odds_square = 0  # number of plots that can be reached by an odd number of steps in the original grid.
    odds_diamond = 0  # number of plots that can be reached by an odd number of steps, after 65 steps from the origin.
    while queue:
        cur, n = queue.pop(0)
        if cur in visited:
            continue
        if n > 130:
            continue
        visited.add(cur)
        r, c = cur
        if n % 2 == 0:
            evens_square += 1
            if n <= 65:
                evens_diamond += 1
        else:
            odds_square += 1
            if n <= 65:
                odds_diamond += 1
        for a, b in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            rr, cc = r + a, c + b
            if not (0 <= rr < len(grid) and 0 <= cc < len(grid[0])):
                continue
            if grid[rr][cc] == '#':
                continue
            queue.append(((rr, cc), n + 1))

    # Since the grids repeat, the parity of each cell in adjacent grids are flipped.
    # This formula I put together by sketching the infinite grid on paper, then calculating the number of "odd" grids and
    # the number of "even" grids. 'n' is the maximum distance of grids that the Elf can reach from the starting grid.
    n = (26501365 - 65) / 131
    print(int(n ** 2 * evens_square + (n - 1) ** 2 * odds_square + n * 4 * odds_square - (n + 1) * (
                odds_square - odds_diamond) + n * (evens_square - evens_diamond)))


part1()
part2()
