def part1():
    f = open("day18input.txt", 'r')

    DIRECTIONS = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}
    edge_vertices = 0

    def shoelace_formula(coordinates):
        n = len(coordinates)
        area = 0.5 * abs(sum(
            coordinates[i][0] * coordinates[(i + 1) % n][1] - coordinates[(i + 1) % n][0] * coordinates[i][1] for i in
            range(n)))
        return int(area)

    path = [(0, 0)]
    y = 0
    x = 0

    for line in f:
        l = line.strip().split()
        n = int(l[1])
        d = l[0]

        a, b = DIRECTIONS[d]
        y, x = y + a * n, x + b * n
        path.append((y, x))
        edge_vertices += n

    # pick's theorem
    print(int(shoelace_formula(path) + 1 + edge_vertices / 2))


def part2():
    f = open("day18input.txt", 'r')

    DIRECTIONS = {'0': (0, 1), '2': (0, -1), '3': (-1, 0), '1': (1, 0)}
    HEX = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12,
           'd': 13, 'e': 14, 'f': 15}

    edge_vertices = 0

    def shoelace_formula(coordinates):
        n = len(coordinates)
        area = 0.5 * abs(sum(
            coordinates[i][0] * coordinates[(i + 1) % n][1] - coordinates[(i + 1) % n][0] * coordinates[i][1] for i in
            range(n)))
        return int(area)

    path = [(0, 0)]
    y = 0
    x = 0

    for line in f:
        l = line.strip().split()
        h = l[2][2:-1]
        n = 0
        for i in range(5):
            n *= 16
            n += HEX[h[i]]
        d = h[5]

        a, b = DIRECTIONS[d]
        y, x = y + a * n, x + b * n
        path.append((y, x))
        edge_vertices += n

    # pick's theorem
    print(int(shoelace_formula(path) + 1 + edge_vertices / 2))


part1()
part2()