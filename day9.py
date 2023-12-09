def part1():
    f = open("day9input.txt", 'r')

    total = 0
    for line in f:
        ns = list(map(int, line.split()))
        nss = [ns]
        cur = []
        for i in range(0, len(ns) - 1):
            cur.append(ns[i + 1] - ns[i])
        while any(n != 0 for n in cur):
            nss.append(cur)
            new_cur = []
            for i in range(0, len(cur) - 1):
                new_cur.append(cur[i + 1] - cur[i])
            cur = new_cur
        nss.append(cur)

        s = 0
        for ns in reversed(nss):
            s += ns[len(ns)-1]
        total += s

    print(total)


def part2():
    f = open("day9input.txt", 'r')

    total = 0
    for line in f:
        ns = list(map(int, line.split()))
        nss = [ns]
        cur = []
        for i in range(0, len(ns)-1):
            cur.append(ns[i+1] - ns[i])
        while any(n != 0 for n in cur):
            nss.append(cur)
            new_cur = []
            for i in range(0, len(cur) - 1):
                new_cur.append(cur[i+1] - cur[i])
            cur = new_cur
        nss.append(cur)

        s = 0
        for ns in reversed(nss):
            s = ns[0] - s
        total += s

    print(total)


part1()
part2()