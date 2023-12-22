def part1():
    f = open("day22input.txt", 'r')

    bricks = []
    heights = [[(0, None)] * 10 for _ in range(10)]

    for line in f:
        a, b = [list(map(int, ns.split(","))) for ns in line.strip().split("~")]
        bricks.append((a, b))

    bricks.sort(key=lambda x: min(x[0][2], x[1][2]))
    supporting = {}
    supported_by = {}

    for id in range(len(bricks)):
        brick = bricks[id]
        (x1, y1, z1), (x2, y2, z2) = brick
        found = set()
        max_height = 0
        supporting[id] = set()
        supported_by[id] = set()

        if x1 != x2:
            for x in range(min(x1, x2), max(x1, x2)+1):
                h, last = heights[x][y1]
                max_height = max(max_height, h)
            for x in range(min(x1, x2), max(x1, x2)+1):
                h, last = heights[x][y1]
                heights[x][y1] = (max_height + 1, id)
                if last is not None and h == max_height:
                    supporting[last].add(id)
                    supported_by[id].add(last)
        elif y1 != y2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                h, last = heights[x1][y]
                max_height = max(max_height, h)
            for y in range(min(y1, y2), max(y1, y2) + 1):
                h, last = heights[x1][y]
                heights[x1][y] = (max_height + 1, id)
                if last is not None and h == max_height:
                    supporting[last].add(id)
                    supported_by[id].add(last)
        else:
            h, last = heights[x1][y1]
            heights[x1][y1] = (h + abs(z1 - z2) + 1, id)
            if last is not None:
                supporting[last].add(id)
                supported_by[id].add(last)

    total = 0

    for id in supporting:
        if len(supporting[id]) == 0:
            total += 1
        else:
            removable = True
            for i in supporting[id]:
                if len(supported_by[i]) == 1:
                    removable = False
                    break
            if removable:
                total += 1

    print(total)


def part2():
    f = open("day22input.txt", 'r')

    bricks = []
    heights = [[(0, None)] * 10 for _ in range(10)]

    for line in f:
        a, b = [list(map(int, ns.split(","))) for ns in line.strip().split("~")]
        bricks.append((a, b))

    bricks.sort(key=lambda x: min(x[0][2], x[1][2]))
    supporting = {}
    supported_by = {}

    for id in range(len(bricks)):
        brick = bricks[id]
        (x1, y1, z1), (x2, y2, z2) = brick
        found = set()
        max_height = 0
        supporting[id] = set()
        supported_by[id] = set()

        if x1 != x2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                h, last = heights[x][y1]
                max_height = max(max_height, h)
            for x in range(min(x1, x2), max(x1, x2) + 1):
                h, last = heights[x][y1]
                heights[x][y1] = (max_height + 1, id)
                if last is not None and h == max_height:
                    supporting[last].add(id)
                    supported_by[id].add(last)
        elif y1 != y2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                h, last = heights[x1][y]
                max_height = max(max_height, h)
            for y in range(min(y1, y2), max(y1, y2) + 1):
                h, last = heights[x1][y]
                heights[x1][y] = (max_height + 1, id)
                if last is not None and h == max_height:
                    supporting[last].add(id)
                    supported_by[id].add(last)
        else:
            h, last = heights[x1][y1]
            heights[x1][y1] = (h + abs(z1 - z2) + 1, id)
            if last is not None:
                supporting[last].add(id)
                supported_by[id].add(last)

    total = 0
    for id in supporting:
        queue = [id]
        falling = set()
        while queue:
            cur = queue.pop(0)
            if cur in falling:
                continue
            falling.add(cur)
            for i in supporting[cur]:
                if all(s in falling for s in supported_by[i]):
                    queue.append(i)
        total += len(falling) - 1

    print(total)


part1()
part2()