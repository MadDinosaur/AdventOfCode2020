# How many passwords are valid according to their policies?
passwords = []
policies = []

while True:
    line = input()
    if line == "end":
        break
    line = line.split(":")
    passwords.append(line[1].strip(" "))
    policies.append(line[0])


def part_one():
    valid_passwords = 0

    for i in range(len(passwords)):
        min = int(policies[i].split("-")[0])
        max = int(policies[i].split("-")[1].split(" ")[0])
        char = policies[i].split(" ")[1]

        occurrences = passwords[i].count(char)

        if occurrences in range(min, max + 1):
            valid_passwords += 1

    print(valid_passwords)


def part_two():
    valid_passwords = 0

    for i in range(len(passwords)):
        first_pos = int(policies[i].split("-")[0])
        second_pos = int(policies[i].split("-")[1].split(" ")[0])
        char = policies[i].split(" ")[1]

        if (passwords[i][first_pos - 1] == char and passwords[i][second_pos - 1] != char) or (passwords[i][first_pos - 1] != char and passwords[i][second_pos - 1] == char):
            valid_passwords += 1

    print(valid_passwords)

