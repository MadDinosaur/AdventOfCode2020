# What is the number of 1-jolt differences multiplied by the number of 3-jolt differences?
adapters = [0]
while True:
    line = input()
    if line == "end":
        break
    adapters.append(int(line))

adapters.append(max(adapters) + 3)


def part_one():
    adapters.sort()
    jolt_diff = [curr - prev for prev, curr in zip(adapters[:-1], adapters[1:])]
    return jolt_diff.count(1) * jolt_diff.count(3)


def part_two():
    adapters.sort()
    total_options = []

    def find_combination(pos):
        options = list(x for x in adapters if adapters[pos] < x <= adapters[pos] + 3)
        if len(options) == 0:
            total_options.append(1)
        for option in options:
            pos += 1
            find_combination(pos)

    find_combination(0)
    return sum(total_options)
