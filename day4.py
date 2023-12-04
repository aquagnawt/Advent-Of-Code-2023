def part1():
    f = open("day4input.txt", 'r')

    total = 0
    for line in f:
        a, b = line.split(":")[1].split("|")
        a = a.strip().split(" ")
        b = b.strip().split(" ")

        score = 0
        for n in a:
            if n == '':
                continue
            if n in b:
                if score == 0:
                    score = 1
                else:
                    score *= 2

        total += score

    print(total)


def part2():
    f = open("day4input.txt", 'r')

    counter = [1] * 194
    id = 0

    for line in f:
        a, b = line.split(":")[1].split("|")
        a = a.strip().split(" ")
        b = b.strip().split(" ")

        score = 0
        for n in a:
            if n == '':
                continue
            if n in b:
                score += 1
        for i in range(id + 1, id + score + 1):
            counter[i] += counter[id]

        id += 1

    print(sum(counter))


part1()
part2()

