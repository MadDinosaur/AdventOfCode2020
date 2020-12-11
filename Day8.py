# Immediately before any instruction is executed a second time, what value is in the accumulator?
instructions = []
while True:
    line = input()
    if line == "end":
        break
    line = line.split(" ")
    instructions.append((line[0], int(line[1])))


def run():
    visited = [0] * len(instructions)
    pos = 0
    acc = 0
    halted = False

    while pos < len(instructions):
        # keeps track of executed instructions
        if visited[pos] == 1:
            halted = True
            break
        else:
            visited[pos] = 1
        # executes the instructions
        if instructions[pos][0] == "jmp":
            pos += instructions[pos][1]
        elif instructions[pos][0] == "nop":
            pos += 1
        else:
            acc += instructions[pos][1]
            pos += 1

    return acc, halted


def part_one():
    print(run())


def part_two():
    pos = 0

    while True:
        (instr, step) = instructions[pos]
        if instr == "jmp":
            instructions[pos] = ("nop", step)
        elif instr == "nop":
            instructions[pos] = ("jmp", step)
        else:
            pos += 1
            continue

        (acc, halted) = run()
        if halted:
            instructions[pos] = (instr, step)
            pos += step if instr == "jmp" else 1
        else:
            print(acc)
            break
