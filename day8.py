import math

def part1():
    f = open("day8input.txt", 'r')

    d = {}
    instructions = f.readline().strip()
    f.readline()

    for line in f:
        l = (line.split("="))
        k = l[0].strip()
        v = l[1].strip().replace("(", "").replace(")", "").split(", ")
        d[k] = (v[0], v[1])

    cur = 'AAA'
    steps = 0
    while cur != 'ZZZ':
        for c in instructions:
            if c == 'R':
                cur = d[cur][1]
            else:
                cur = d[cur][0]
            steps += 1

    print(steps)


def part2():
    def lcm(ns):
        result = ns[0]
        for n in ns[1:]:
            result = abs(result*n) // math.gcd(result, n)
        return result

    f = open("day8input.txt", 'r')

    d = {}
    instructions = f.readline().strip()
    f.readline()

    start = set()
    for line in f:
        l = (line.split("="))
        k = l[0].strip()
        v = l[1].strip().replace("(", "").replace(")", "").split(", ")
        d[k] = (v[0], v[1])
        if k[2] == 'A':
            start.add(k)


    all_steps = []
    for k in start:
        cur = k
        steps = 0
        while cur[2] != 'Z':
            for c in instructions:
                if c == 'R':
                    cur = d[cur][1]
                else:
                    cur = d[cur][0]
                steps += 1
        all_steps.append(steps)

    print(lcm(all_steps))


part1()
part2()