# Find the two entries that sum to 2020; what do you get if you multiply them together?
try:
    numbers = []

    while True:
        numbers.append(int(input()))

except:
    print("input finalized")

year = 2020


def part_one():
    found = False
    i = 0

    while not found:
        number_to_search = year - numbers[i]
        if number_to_search < 0:
            i += 1
        elif number_to_search in numbers:
            found = True
        else:
            i += 1

    print(number_to_search, numbers[i])
    print(number_to_search * numbers[i])


def partTwo():
    numbers.sort()
    for i in range(0, len(numbers) - 2):
        l = i + 1
        r = len(numbers) - 1
        while l < r:
            if numbers[i] + numbers[l] + numbers[r] == year:
                print(numbers[i], numbers[l], numbers[r])
                print(numbers[i] * numbers[l] * numbers[r])
                break
            elif numbers[i] + numbers[l] + numbers[r] < year:
                l += 1
            else:
                r -= 1


