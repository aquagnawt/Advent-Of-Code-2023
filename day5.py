def part1():
    f = open("day5input.txt", 'r')

    m = 1e20
    sources = map(int, f.readline().split(":")[1].strip().split())
    f.readline()

    maps = [[], [], [], [], [], [], []]

    id = 0
    for line in f:
        if line[0].isnumeric():
            maps[id].append(list(map(int, line.split())))
        if line == '\n':
            id += 1

    for s in sources:

        for i in range(7):
            for ma in maps[i]:
                a = ma[0]
                b = ma[1]
                c = ma[2]
                if b <= s < b+c:
                    s += a - b
                    break

        m = min(m, s)

    print(m)


def part2():
    f = open("day5input.txt", 'r')

    m = 1e20
    sources = list(map(int, f.readline().split(":")[1].strip().split()))
    f.readline()

    maps = [[], [], [], [], [], [], []]

    id = 0
    for line in f:
        if line[0].isnumeric():
            maps[id].append(list(map(int, line.split())))
        if line == '\n':
            id += 1

    intervals = []
    for x in range(0, len(sources), 2):
        intervals.append((sources[x], sources[x] + sources[x + 1]))

    for i in range(7):
        temp_se = []
        temp = []
        for (x, y) in intervals:
            for ma in maps[i]:
                a = ma[0]
                b = ma[1]
                c = ma[2]
                max_s = max(x, b)
                min_t = min(y, b + c)

                if max_s < min_t:
                    temp_se.append((max_s + a - b, min_t + a - b))
                    temp.append((max_s, min_t))

            # calculate remainder of the interval that did not satisfy any map
            rem = [(x, y)]
            for (x2, y2) in temp:
                t = []
                removing = []
                for (x3, y3) in rem:
                    max_s = max(x2, x3)
                    min_t = min(y2, y3)
                    if max_s < min_t:
                        if min(x2, x3) < max(x2, x3):
                            t.append((min(x2, x3), max(x2, x3)))
                        if min(y2, y3) < max(y2, y3):
                            t.append((min(y2, y3), max(y2, y3)))
                        removing.append((x3, y3))
                for a in removing:
                    rem.remove(a)
                rem += t
            temp_se += rem

        intervals = temp_se

    for (x, y) in intervals:
        m = min(m, x)

    print(m)


part1()
part2()
