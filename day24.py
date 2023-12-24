from sympy import symbols, solve
from collections import namedtuple

def part1():
    f = open("day24input.txt", 'r')
    Coords = namedtuple('Coords', ['x', 'y', 'z'])

    hailstones = []
    total = 0
    for line in f:
        line = list(map(int, line.replace(" @", ",").split(", ")))
        pos, vel = line[:3], line[3:]
        pos = Coords(pos[0], pos[1], pos[2])
        vel = Coords(vel[0], vel[1], vel[2])

        for other_pos, other_vel in hailstones:
            old_pos = Coords(other_pos.x, other_pos.y, other_pos.z)
            old_vel = Coords(other_vel.x, other_vel.y, other_vel.z)
            other_pos = Coords(pos.x, (pos.x-other_pos.x)/other_vel.x*other_vel.y+other_pos.y, 0)
            other_vel = Coords(vel.x, other_vel.y*(vel.x/other_vel.x), 0)
            if pos == other_pos:
                continue
            elif other_vel.y != vel.y:
                t = (pos.y - other_pos.y)/(other_vel.y - vel.y)
                x = pos.x + vel.x*t
                y = pos.y + vel.y*t
                if (x > pos.x and vel.x <= 0) or (x > old_pos.x and old_vel.x <= 0):
                    continue
                if (x < pos.x and vel.x >= 0) or (x < old_pos.x and old_vel.x >= 0):
                    continue
                if all(200000000000000 <= n <= 400000000000000 for n in [x, y]):
                    total += 1

        hailstones.append((pos, vel))

    print(total)


def part2():
    f = open("day24input.txt", 'r')
    Coords = namedtuple('Coords', ['x', 'y', 'z'])

    hailstones = []
    for line in f:
        line = list(map(int, line.replace(" @", ",").split(", ")))
        pos, vel = line[:3], line[3:]
        hailstones.append((Coords(pos[0], pos[1], pos[2]), Coords(vel[0], vel[1], vel[2])))

    equations = []
    x,y,z,vx,vy,vz = symbols('x,y,z,vx,vy,vz')
    ts = []
    for i in range(len(hailstones)):
        ts.append(symbols(f't{i}'))
    for i, (pos, vel) in enumerate(hailstones):
        equations.append(x+ts[i]*vx-pos.x-ts[i]*vel.x)
        equations.append(y+ts[i]*vy-pos.y-ts[i]*vel.y)
        equations.append(z+ts[i]*vz-pos.z-ts[i]*vel.z)
        result = [s for s in solve(equations) if all(n % 1 == 0 for n in s.values())]
        if len(result) == 1:
            print(result[0][x] + result[0][y] + result[0][z])
            break


part1()
part2()
