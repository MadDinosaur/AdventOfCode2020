# What is the first number that is not the sum of two of the 25 numbers before it?
numbers = []
while True:
    line = input()
    if line == "end":
        break
    numbers.append(int(line))


def part_one():
    pos = 25  # start at index 25

    while True:
        preamble = set(numbers[pos - 25: pos])  # get 25 preceding numbers
        sum = numbers[pos]  # get target number for sum

        found = False  # flag to find the intruder number

        for num1 in preamble:
            num2 = sum - num1
            if num1 != num2 and num2 in preamble:
                found = True
                break

        if found:
            pos += 1
        else:
            return sum
            break


def part_two():
    target = part_one()
    pos = 0

    while pos < len(numbers):
        sum = 0
        sum_index = pos
        while sum < target:
            sum += numbers[sum_index]
            sum_index += 1

        if sum == target:
            return min(numbers[pos:sum_index]) + max(numbers[pos:sum_index])

        pos += 1

