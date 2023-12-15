def part1():
    f = open("day15input.txt", 'r')

    def hash(string):
        t = 0
        for c in string:
            t += ord(c)
            t *= 17
            t = t % 256
        return t

    total = 0
    for line in f:
        strings = line.strip().split(',')
        for s in strings:
            total += hash(s)

    print(total)


def part2():
    f = open("day15input.txt", 'r')

    bins = [[] for _ in range(256)]

    def hash(string):
        t = 0
        for c in string:
            t += ord(c)
            t *= 17
            t = t % 256
        return t

    strings = None
    total = 0
    for line in f:
        strings = line.strip().split(',')
        for s in strings:
            total += hash(s)

    for s in strings:
        if '=' in s:
            key, value = s.split("=")
            value = int(value)
            bin_id = hash(key)
            found = False
            for i in range(len(bins[bin_id])):
                k, v = bins[bin_id][i]
                if k == key:
                    bins[bin_id][i] = (k, value)
                    found = True
            if not found:
                bins[bin_id].append((key, value))
        elif '-' in s:
            key = s.replace('-', '')
            bin_id = hash(key)
            for k, v in bins[bin_id]:
                if k == key:
                    bins[bin_id].remove((k, v))

    total = 0
    for i in range(len(bins)):
        bin = bins[i]
        for j in range(len(bin)):
            _, v = bin[j]
            total += (i + 1) * (j + 1) * v

    print(total)


part1()
part2()