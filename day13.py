def part1():
    f = open("day13input.txt", 'r')

    patterns = []

    cur = []
    for line in f:
        if line == '\n':
            patterns.append(cur)
            cur = []
        else:
            cur.append(line.strip())

    patterns.append(cur)

    patterns_t = []
    for pattern in patterns:
        pattern_t = []
        for c in range(len(pattern[0])):
            col = ""
            for r in range(len(pattern)):
                col += (pattern[r][c])
            pattern_t.append(col)
        patterns_t.append(pattern_t)

    total = 0
    for id in range(len(patterns)):
        pattern = patterns_t[id]
        for i in range(1, len(pattern)):
            l = min(i, len(pattern) - i)
            if pattern[i - l:i] == list(reversed(pattern[i:i + l])):
                total += i
        pattern = patterns[id]
        for i in range(1, len(pattern)):
            l = min(i, len(pattern) - i)
            if pattern[i - l:i] == list(reversed(pattern[i:i + l])):
                total += i * 100

    print(total)


def part2():
    f = open("day13input.txt", 'r')

    patterns = []

    cur = []
    for line in f:
        if line == '\n':
            patterns.append(cur)
            cur = []
        else:
            cur.append(line.strip())

    patterns.append(cur)

    def count_differences(l1, l2):
        count = 0
        for i in range(len(l1)):
            for (c1, c2) in zip(l1[i], l2[i]):
                if c1 != c2:
                    count += 1
        return count

    patterns_t = []
    for pattern in patterns:
        pattern_t = []
        for c in range(len(pattern[0])):
            col = ""
            for r in range(len(pattern)):
                col += (pattern[r][c])
            pattern_t.append(col)
        patterns_t.append(pattern_t)

    total = 0
    for id in range(len(patterns)):
        pattern = patterns_t[id]
        for i in range(1, len(pattern)):
            l = min(i, len(pattern)-i)
            if count_differences(pattern[i-l:i], list(reversed(pattern[i:i+l]))) == 1:
                total += i
        pattern = patterns[id]
        for i in range(1, len(pattern)):
            l = min(i, len(pattern) - i)
            if count_differences(pattern[i-l:i], list(reversed(pattern[i:i+l]))) == 1:
                total += i*100

    print(total)


part1()
part2()
