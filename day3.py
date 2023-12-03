def part1():
    f = open("day3input.txt", "r")

    adj = {(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)}

    lines = []

    for line in f:
        lines.append(line)

    s = {'*', '&', '@', '/', '+', '#', '$', '%', '=', '-'}

    total = 0
    for i in range(len(lines)):
        found = False
        value = 0
        for j in range(len(lines[i])):
            c = lines[i][j]
            if c.isnumeric():
                value = 10 * value + int(c)
                for pair in adj:
                    x, y = pair
                    ii = i + x
                    jj = j + y
                    if ii < 0 or jj < 0 or ii >= len(lines) or jj >= len(lines[i]):
                        continue
                    if lines[ii][jj] in s:
                        found = True
            else:
                if value != 0:
                    if found:
                        total += value
                    value = 0
                    found = False
    print(total)
    f.close()


def part2():
    f = open("day3input.txt", "r")

    adj = {(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)}

    lines = []

    for line in f:
        lines.append(line)

    s = {'*', '&', '@', '/', '+', '#', '$', '%', '=', '-'}
    values = [[1] * len(lines[0]) for i in range(len(lines))]
    counters = [[0] * len(lines[0]) for i in range(len(lines))]

    total = 0
    for i in range(len(lines)):
        found = False
        symbols = []
        value = 0
        for j in range(len(lines[i])):
            c = lines[i][j]
            if c.isnumeric():
                value = 10 * value + int(c)
                for pair in adj:
                    x, y = pair
                    ii = i + x
                    jj = j + y
                    if ii < 0 or jj < 0 or ii >= len(lines) or jj >= len(lines[i]):
                        continue
                    if lines[ii][jj] in s:
                        if (ii, jj) not in symbols:
                            symbols.append((ii, jj))
                        found = True
            else:
                if value != 0:
                    if found:
                        for (x, y) in symbols:
                            values[x][y] *= value
                            counters[x][y] += 1
                    value = 0
                    found = False
                    symbols = []

    for i in range(len(values)):
        for j in range(len(values[i])):
            if counters[i][j] == 2:
                total += values[i][j]

    print(total)
    f.close()


part1()
part2()

