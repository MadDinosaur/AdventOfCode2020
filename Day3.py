# Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?
import math

forest = []
while True:
    line = input()
    if line == "end":
        break
    forest.append(line)

# repeat pattern to the right
num_columns = 7 * len(forest)
while len(forest[0]) < num_columns:
    for i in range(len(forest)):
        forest[i] += forest[i]


def part_one():
    pos = 0
    num_trees = 0
    for i in range(len(forest)):
        if forest[i][pos] == "#":
            num_trees += 1
        pos += 3

    print(num_trees)


def part_two():
    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    num_trees = []

    for i in range(len(slopes)):
        pos = 0
        num_trees_slope = 0
        for j in range(0, len(forest), slopes[i][1]):
            if forest[j][pos] == "#":
                num_trees_slope += 1
            pos += slopes[i][0]
        num_trees.append(num_trees_slope)

    print(num_trees)
    print(math.prod(num_trees))


part_two()
