# For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?
def part_one():
    group_answers = []
    answers = set()
    while True:
        line = input()
        if line == "end":
            group_answers.append(answers)
            break
        if line != "":
            for char in line:
                answers.add(char)
        else:
            group_answers.append(answers)
            answers = set()

    total = sum([len(answer) for answer in group_answers])

    print(total)


def part_two():
    group_answers = []
    answers = []
    while True:
        line = input()
        if line == "end":
            group_answers.append(answers)
            break
        if line != "":
            answers.append(list(line))
        else:
            group_answers.append(answers)
            answers = []

    for i in range(len(group_answers)):
        intersection = set(group_answers[i][0])
        for j in range(1, len(group_answers[i])):
            intersection &= set(group_answers[i][j])
        group_answers[i] = intersection

    total = sum([len(answer) for answer in group_answers])
    print(total)

