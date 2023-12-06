def part1():
    f = open("day6input.txt", 'r')

    times = list(map(int, f.readline().split(":")[1].strip().split()))
    distances = list(map(int, f.readline().split(":")[1].strip().split()))

    total = 1
    for i in range(len(times)):
        count = 0
        for j in range(times[i]+1):
            if (times[i]-j) * j > distances[i]:
                count += 1
        total *= count

    print(total)


def part2():
    f = open("day6input.txt", 'r')

    times = int(f.readline().split(":")[1].strip().replace(" ", ""))
    distances = int(f.readline().split(":")[1].strip().replace(" ", ""))

    count = 0
    for j in range(times + 1):
        if (times - j) * j > distances:
            count += 1

    print(count)


part1()
part2()

