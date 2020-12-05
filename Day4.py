# In your batch file, how many passports are valid?
import re

passports = []
passport = {}
while True:
    line = input()
    if line == "end":
        passports.append(passport)
        break
    if line != "":
        line = re.split(':| ', line)
        for i in range(0, len(line), 2):
            passport[line[i]] = line[i+1]
    else:
        passports.append(passport)
        passport = {}

fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def part_one():
    valid_passports = 0

    for passport in passports:
        if set(fields).issubset(passport.keys()):
            valid_passports += 1

    print(valid_passports)


def part_two():
    valid_passports = 0

    for passport in passports:
        # first validation
        if set(fields).issubset(passport.keys()):
            # second validation
            if not re.search('(?=^([0-9]{4})$)(?:19[2-9][0-9]|200[0-2])', passport["byr"]):
                continue
            if not re.search('(?=^([0-9]{4})$)(?:20[1][0-9]|2020)', passport["iyr"]):
                continue
            if not re.search('(?=^([0-9]{4})$)(?:20[2][0-9]|2030)', passport["eyr"]):
                continue
            if not re.search('((?=^([0-9]{3}))(?:1[5-8][0-9]|19[0-3])(?=cm$))|((?=^([0-9]{2}))(?:59|6[0-9]|7[0-6])(?=in$))', passport["hgt"]):
                continue
            if not re.search('^#[0-9a-f]{6}$', passport["hcl"]):
                continue
            if not re.search('^(amb|blu|brn|gry|grn|hzl|oth)$', passport["ecl"]):
                continue
            if not re.search('^([0-9]{9})$', passport["pid"]):
                continue
            valid_passports += 1

    print(valid_passports)
