# How many bag colors can eventually contain at least one shiny gold bag?
import re

rules = []
while True:
    line = input()

    if line == "end":
        break

    line = re.split(" bags| bag| contain |, ", line)
    outer = line[0]
    inner = " ".join(line[2: -1])
    rules.append((outer, inner))
rules_dict = dict(rules)


def part_one():
    bags = ["shiny gold"]
    for bag in bags:
        for outer, inner in rules:
            if (bag in inner) and (outer not in bags):
                bags.append(outer)
    print(len(bags) - 1)


def part_two():
    print(number_of_bags("shiny gold"))


def number_of_bags(bag):
    total = 0
    contents = rules_dict[bag].split("  ")
    for sub in contents:
        if sub.strip("  ") == "no other":
            return 0
        total += int(sub[0]) + int(sub[0]) * number_of_bags(sub[1: len(sub)].strip(" "))
    return total

