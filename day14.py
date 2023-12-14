def part1():
    f = open("day14input.txt", 'r')

    platform = []

    for line in f:
        platform.append(line.strip())

    total = 0
    for c in range(len(platform[0])):
        load = len(platform)
        for r in range(len(platform)):
            if platform[r][c] == '#':
                load = len(platform) - r - 1
            elif platform[r][c] == 'O':
                total += load
                load -= 1

    print(total)


def part2():
    import copy

    f = open("day14input.txt", 'r')

    platform = []

    for line in f:
        platform.append([*line.strip()])

    memo = []
    found_index = -1
    for i in range(1000000000):
        if platform in memo:
            found_index = memo.index(platform)
            break

        memo.append(copy.deepcopy(platform))

        for c in range(len(platform[0])):
            i = 0
            for r in range(len(platform)):
                if platform[r][c] == '#':
                    i = r + 1
                elif platform[r][c] == 'O':
                    platform[r][c] = '.'
                    platform[i][c] = 'O'
                    i += 1

        for r in range(len(platform)):
            i = 0
            for c in range(len(platform[0])):
                if platform[r][c] == '#':
                    i = c + 1
                elif platform[r][c] == 'O':
                    platform[r][c] = '.'
                    platform[r][i] = 'O'
                    i += 1

        for c in range(len(platform[0])):
            i = len(platform) - 1
            for r in range(len(platform) - 1, -1, -1):
                if platform[r][c] == '#':
                    i = r - 1
                elif platform[r][c] == 'O':
                    platform[r][c] = '.'
                    platform[i][c] = 'O'
                    i -= 1

        for r in range(len(platform)):
            i = len(platform) - 1
            for c in range(len(platform[0]) - 1, -1, -1):
                if platform[r][c] == '#':
                    i = c - 1
                elif platform[r][c] == 'O':
                    platform[r][c] = '.'
                    platform[r][i] = 'O'
                    i -= 1

    id = 1000000000
    if found_index != -1:
        id = found_index + (1000000000 - found_index) % (len(memo) - found_index)
    platform = memo[id]

    total = 0
    for i, line in enumerate(platform):
        total += line.count('O') * (len(platform) - i)

    print(total)


part1()
part2()
