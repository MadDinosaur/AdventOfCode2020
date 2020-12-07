# What is the highest seat ID on a boarding pass?
import math

boarding_passes = []
while True:
    line = input()
    if line == "end":
        break
    boarding_passes.append(line)


# converts a row and column number into a seat code
def convert(row, column):
    new_boarding_pass = ""
    for i in range(7):
        if row & 0b1000000:
            new_boarding_pass += "B"
        else:
            new_boarding_pass += "F"
        row = row << 1
    for i in range(3):
        if column & 0b100:
            new_boarding_pass += "R"
        else:
            new_boarding_pass += "L"
        column = column << 1
    return new_boarding_pass


def part_one():
    highest_row = 127
    highest_column = 7
    boarding_pass = convert(highest_row, highest_column)

    # tries the highest possible combinations until it finds an existing one
    while boarding_pass not in boarding_passes:
        highest_column -= 1

        if highest_column == -1:
            highest_column = 7
            highest_row -= 1

        boarding_pass = convert(highest_row, highest_column)

    print(boarding_pass, highest_row * 8 + highest_column)


def verify(seat_id):
    binary_id = str(bin(seat_id))

    row_id = binary_id[2: 9]
    column_id = binary_id[9: 12]

    row_id = row_id.replace("1", "B")
    row_id = row_id.replace("0", "F")

    column_id = column_id.replace("1", "R")
    column_id = column_id.replace("0", "L")

    return row_id+column_id in boarding_passes


def part_two():
    row = 127
    column = 7
    while row != 0 or column != 0:
        boarding_pass = convert(row, column)
        seat_id = row * 8 + column

        if boarding_pass not in boarding_passes:
            if verify(seat_id + 1) and verify(seat_id - 1):
                print(boarding_pass, seat_id)
                break

        column -= 1
        if column == -1:
            column = 7
            row -= 1


part_two()
