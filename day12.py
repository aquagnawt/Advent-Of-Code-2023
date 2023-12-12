def part1():
    f = open("day12input.txt", 'r')

    def count(field, groups, f_id, g_id, g_len):
        if f_id >= len(field):
            if g_id == len(groups)-1 and g_len == groups[g_id]:
                return 1
            if g_id == len(groups) and g_len == 0:
                return 1
            else:
                return 0

        ans = 0

        if field[f_id] == '#' or field[f_id] == '?':
            ans += count(field, groups, f_id+1, g_id, g_len+1)

        if field[f_id] == '.' or field[f_id] == '?':
            if g_len == 0:
                ans += count(field, groups, f_id+1, g_id, g_len)
            elif g_id < len(groups) and groups[g_id] == g_len:
                ans += count(field, groups, f_id+1, g_id+1, 0)

        return ans

    total = 0
    for line in f:
        l = (line.strip().split())
        field = l[0]
        groups = list(map(int, l[1].split(',')))
        total += count(field, groups, 0, 0, 0)

    print(total)


def part2():
    f = open("day12input.txt", 'r')

    def count(field, groups, f_id, g_id, g_len):
        if (f_id, g_id, g_len) in dp:
            return dp[(f_id, g_id, g_len)]

        if f_id >= len(field):
            if g_id == len(groups) - 1 and g_len == groups[g_id]:
                return 1
            if g_id == len(groups) and g_len == 0:
                return 1
            else:
                return 0

        ans = 0

        if field[f_id] == '#' or field[f_id] == '?':
            ans += count(field, groups, f_id + 1, g_id, g_len + 1)

        if field[f_id] == '.' or field[f_id] == '?':
            if g_len == 0:
                ans += count(field, groups, f_id + 1, g_id, g_len)
            elif g_id < len(groups) and groups[g_id] == g_len:
                ans += count(field, groups, f_id + 1, g_id + 1, 0)

        dp[(f_id, g_id, g_len)] = ans

        return ans

    total = 0
    for line in f:
        l = (line.strip().split())
        field = '?'.join([l[0]] * 5)
        groups = list(map(int, (','.join([l[1]] * 5)).split(',')))
        dp = {}
        total += count(field, groups, 0, 0, 0)

    print(total)


part1()
part2()
