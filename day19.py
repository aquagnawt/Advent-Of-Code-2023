def part1():
    f = open("day19input.txt", 'r')

    instructions = {}

    line = f.readline()
    while line != "\n":
        l = line.split("{")
        name = l[0]
        i = l[1].strip()[:-1].split(',')

        instructions[name] = i

        line = f.readline()

    total = 0
    for line in f:
        l = line.strip()[1:-1].split(',')
        vals = {}
        for a in l:
            n, x = a.split('=')
            vals[n] = int(x)

        cur = 'in'
        while cur != 'R' and cur != 'A':
            for i in instructions[cur]:
                if '<' in i:
                    z, c = i.split(':')
                    a, b = z.split('<')
                    if vals[a] < int(b):
                        cur = c
                        break
                elif '>' in i:
                    z, c = i.split(':')
                    a, b = z.split('>')
                    if vals[a] > int(b):
                        cur = c
                        break
                else:
                    cur = i

        if cur == 'A':
            total += sum(vals.values())

    print(total)


def part2():
    f = open("day19input.txt", 'r')

    instructions = {}

    line = f.readline()
    while line != "\n":
        l = line.split("{")
        instructions[l[0]] = l[1].strip()[:-1].split(',')
        line = f.readline()

    ranges = []

    def check_valid(ranges):
        for r1, r2 in ranges:
            if r1 > r2:
                return False
        return True

    def go(cur, cur_ranges):
        new_ranges = dict(cur_ranges)
        for i in instructions[cur]:
            if not check_valid(cur_ranges.values()):
                return
            if '<' in i:
                z, c = i.split(':')
                a, b = z.split('<')
                r = dict(new_ranges)
                r[a] = (r[a][0], min(r[a][1], int(b) - 1))
                if c == 'A':
                    ranges.append(r)
                elif c != 'R':
                    go(c, r)
                new_ranges[a] = (max(new_ranges[a][0], int(b)), new_ranges[a][1])
            elif '>' in i:
                z, c = i.split(':')
                a, b = z.split('>')
                r = dict(new_ranges)
                r[a] = (max(r[a][0], int(b) + 1), r[a][1])
                if c == 'A':
                    ranges.append(r)
                elif c != 'R':
                    go(c, r)
                new_ranges[a] = (new_ranges[a][0], min(new_ranges[a][1], int(b)))
            else:
                if i == 'A':
                    ranges.append(new_ranges)
                elif i != 'R':
                    go(i, new_ranges)

    go('in', {'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)})

    total = 0
    for r in ranges:
        t = 1
        for a, b in r.values():
            t *= b - a + 1
        total += t

    print(total)


part1()
part2()
