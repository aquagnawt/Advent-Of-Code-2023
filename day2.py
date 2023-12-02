def part1():
    f = open("day2input.txt", "r")

    bag = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    game = 1
    total = 0
    s = f.readline()
    while s != "":
        grabs = list(map(lambda x: x.split(","), s.split(":")[1].split(";")))
        impossible = False
        for grab in grabs:
            for colour in grab:
                temp = colour.split(" ")
                n = int(temp[1])
                col = temp[2].strip()
                if n > bag[col]:
                    impossible = True
                    break
            if impossible:
                break
        if not impossible:
            total += game
        s = f.readline()
        game += 1
    f.close()
    print(total)


def part2():
    f = open("day2input.txt", "r")
    s = f.readline()
    total = 0
    game = 1
    while s != "":
        grabs = list(map(lambda x: x.split(","), s.split(":")[1].split(";")))

        bag = {
            "red": 0,
            "green": 0,
            "blue": 0
        }

        for grab in grabs:
            for colour in grab:
                temp = colour.split(" ")
                n = int(temp[1])
                col = temp[2].strip()
                if n > bag[col]:
                    bag[col] = n
        total += bag["red"] * bag["green"] * bag["blue"]
        s = f.readline()
        game += 1
    f.close()
    print(total)


part1()
part2()
