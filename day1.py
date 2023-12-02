def part1():
    f = open("day1input.txt", "r")

    s = f.readline()
    total = 0
    while s != "":
        first = -1
        last = -1
        for i in range(len(s)):
            if s[i].isnumeric():
                if first == -1:
                    first = int(s[i])
                last = int(s[i])
        total += first * 10 + last
        s = f.readline()
    f.close()
    print(total)

def part2():
    f = open("day1input.txt", "r")

    digits = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10
    }

    s = f.readline()
    total = 0
    while s != "":
        first = -1
        last = -1
        for i in range(len(s)):
            if s[i].isnumeric():
                if first == -1:
                    first = int(s[i])
                last = int(s[i])
            for j in range(3, 6):
                if s[i:i+j] in digits:
                    n = digits[s[i:i+j]]
                    if first == -1:
                        first = n
                    last = n
        total += first * 10 + last
        s = f.readline()
    f.close()
    print(total)


part1()
part2()
