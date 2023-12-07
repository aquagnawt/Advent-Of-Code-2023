def part1():
    f = open("day7input.txt", 'r')

    # fives, fours, fulls, threes, twos, ones, highs
    scores = [[], [], [], [], [], [], [], []]

    for line in f:
        l = line.split()
        hand = l[0]
        val = int(l[1])

        values = {
            '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, 'T': 0, 'J': 0, 'Q': 0, 'K': 0, 'A': 0,
        }

        for card in hand:
            values[card] += 1

        c5 = 0
        c4 = 0
        c3 = 0
        c2 = 0
        for v in values:
            if values[v] == 5:
                c5 += 1
            elif values[v] == 4:
                c4 += 1
            elif values[v] == 3:
                c3 += 1
            elif values[v] == 2:
                c2 += 1
        if c5 > 0:
            scores[0].append((hand, val))
        elif c4 > 0:
            scores[1].append((hand, val))
        elif c3 == 1 and c2 == 1:
            scores[2].append((hand, val))
        elif c3 > 0:
            scores[3].append((hand, val))
        elif c2 == 2:
            scores[4].append((hand, val))
        elif c2 == 1:
            scores[5].append((hand, val))
        else:
            scores[6].append((hand, val))

    rank = 1
    total = 0
    for s in reversed(scores):
        for pair in sorted(s, key = lambda x : x[0].replace("T", "B").replace("K", "S").replace("A", "Z")):
            total += pair[1]*rank
            rank += 1
    print(total)


def part2():
    f = open("day7input.txt", 'r')

    # fives, fours, fulls, threes, twos, ones, highs
    scores = [[], [], [], [], [], [], [], []]

    for line in f:
        l = line.split()
        hand = l[0]
        val = int(l[1])
        values = {
            '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, 'T': 0, 'J': 0, 'Q': 0, 'K': 0, 'A': 0
        }

        for card in hand:
            values[card] += 1

        highest = 0
        highest_value = 'J'
        for v in values:
            if v == 'J':
                continue
            if values[v] > highest:
                highest = values[v]
                highest_value = v
        new_hand = hand.replace('J', highest_value)

        values = {
            '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, 'T': 0, 'J': 0, 'Q': 0, 'K': 0, 'A': 0
        }

        for card in new_hand:
            values[card] += 1

        c5 = 0
        c4 = 0
        c3 = 0
        c2 = 0
        for v in values:
            if values[v] == 5:
                c5 += 1
            elif values[v] == 4:
                c4 += 1
            elif values[v] == 3:
                c3 += 1
            elif values[v] == 2:
                c2 += 1
        if c5 > 0:
            scores[0].append((hand, val))
        elif c4 > 0:
            scores[1].append((hand, val))
        elif c3 == 1 and c2 == 1:
            scores[2].append((hand, val))
        elif c3 > 0:
            scores[3].append((hand, val))
        elif c2 == 2:
            scores[4].append((hand, val))
        elif c2 == 1:
            scores[5].append((hand, val))
        else:
            scores[6].append((hand, val))

    rank = 1
    total = 0
    for s in reversed(scores):
        for pair in sorted(s,
                           key=lambda x: x[0].replace("T", "M").replace("K", "S").replace("A", "Z").replace("J", "0")):
            total += pair[1] * rank
            rank += 1
    print(total)


part1()
part2()
