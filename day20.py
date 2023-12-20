def part1():
    f = open("day20input.txt", 'r')

    start = []
    flipflops = {}
    conjunctions = {}
    sources = {}

    class Flipflop:
        def __init__(self, name, targets):
            self.name = name
            self.targets = targets
            self.strength = 0

    class Conjunction:
        def __init__(self, name, targets):
            self.name = name
            self.sources = []
            self.targets = targets

    for line in f:
        line = line.strip()
        if '%' in line:
            s, t = line[1:].split(" -> ")
            t = t.split(", ")
            flipflops[s] = Flipflop(s, t)
            for d in t:
                if d not in sources:
                    sources[d] = []
                sources[d].append((0, s))
        elif '&' in line:
            s, t = line[1:].split(" -> ")
            t = t.split(", ")
            conjunctions[s] = Conjunction(s, t)
            for d in t:
                if d not in sources:
                    sources[d] = []
                sources[d].append((0, s))
        else:
            targets = line.split(" -> ")[1].split(", ")
            start = [(0, 'broadcaster', t) for t in targets]
            for d in targets:
                if d not in sources:
                    sources[d] = []
                sources[d].append((0, 'broadcaster'))

    for c in conjunctions:
        if c in sources:
            conjunctions[c].sources = sources[c]

    low_count = 0
    high_count = 0

    for i in range(1000):
        low_count += 1
        queue = list(start)
        while queue:
            strength, source, current = queue.pop(0)
            if strength:
                high_count += 1
            else:
                low_count += 1
            # print(f"{source} {strength}> {current}")
            if current in flipflops:
                if strength == 0:
                    flipflops[current].strength = (flipflops[current].strength + 1) % 2
                    for t in flipflops[current].targets:
                        queue.append((flipflops[current].strength, current, t))
            elif current in conjunctions:
                sending = 0
                for i, (s, name) in enumerate(conjunctions[current].sources):
                    if name == source:
                        conjunctions[current].sources[i] = (strength, name)
                        if strength == 0:
                            sending = 1
                            break
                    else:
                        if s == 0:
                            sending = 1
                for t in conjunctions[current].targets:
                    queue.append((sending, current, t))

    print(low_count * high_count)


def part2():
    import math

    f = open("day20input.txt", 'r')

    start = []
    flipflops = {}
    conjunctions = {}
    sources = {}
    final_conj = set()

    class Flipflop:
        def __init__(self, name, targets):
            self.name = name
            self.targets = targets
            self.strength = 0

        def __eq__(self, other):
            return self.name == other.name and self.strength == other.strength

    class Conjunction:
        def __init__(self, name, targets):
            self.name = name
            self.sources = []
            self.targets = targets

        def __eq__(self, other):
            return self.name == other.name and self.sources == other.sources

    for line in f:
        line = line.strip()
        if '%' in line:
            s, t = line[1:].split(" -> ")
            t = t.split(", ")
            flipflops[s] = Flipflop(s, t)
            for d in t:
                if d not in sources:
                    sources[d] = []
                sources[d].append((0, s))
                if d == 'kz':  # kz directs to rx
                    final_conj.add(s)
        elif '&' in line:
            s, t = line[1:].split(" -> ")
            t = t.split(", ")
            conjunctions[s] = Conjunction(s, t)
            for d in t:
                if d not in sources:
                    sources[d] = []
                sources[d].append((0, s))
                if d == 'kz':  # kz directs to rx
                    final_conj.add(s)
        else:
            targets = line.split(" -> ")[1].split(", ")
            start = [(0, 'broadcaster', t) for t in targets]
            for d in targets:
                if d not in sources:
                    sources[d] = []
                sources[d].append((0, 'broadcaster'))

    for c in conjunctions:
        if c in sources:
            conjunctions[c].sources = sources[c]

    button_presses = 0
    finished = False
    cycles = []

    while True:
        button_presses += 1
        queue = list(start)
        while queue:
            strength, source, current = queue.pop(0)
            if current == 'kz' and source in final_conj and strength == 1:
                cycles.append(button_presses)
                final_conj.remove(source)
            if len(final_conj) == 0:
                finished = True
                break
            if current in flipflops:
                if strength == 0:
                    flipflops[current].strength = (flipflops[current].strength + 1) % 2
                    for t in flipflops[current].targets:
                        queue.append((flipflops[current].strength, current, t))
            elif current in conjunctions:
                sending = 0
                for i, (s, name) in enumerate(conjunctions[current].sources):
                    if name == source:
                        conjunctions[current].sources[i] = (strength, name)
                        if strength == 0:
                            sending = 1
                            break
                    else:
                        if s == 0:
                            sending = 1
                for t in conjunctions[current].targets:
                    queue.append((sending, current, t))

        if finished:
            break

    def lcm(ns):
        result = ns[0]
        for n in ns[1:]:
            result = abs(result * n) // math.gcd(result, n)
        return result

    print(lcm(cycles))


part1()
part2()
