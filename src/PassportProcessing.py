# Day 4 Passport Processing

"""
Takes the text file and converts the passports to an array of maps

Extra processing was needed as the format of the passport text file is not consistent:
    You could have a passport all on one line, separated by newlines, or inconsistently separated
"""
def get_passports():
    passports = []
    with open('../assets/passports.txt', 'r') as f:
        unformatted_passports = f.readlines()
        f.close()

    formatted_passport = ""
    i = 0
    for passport in unformatted_passports:

        #Edge case for last passport in the file.  Could have added a newline to the file but ¯\_(ツ)_/¯
        if i == len(unformatted_passports):
            formatted_passport += passport.replace("\n", " ")

        #All passports are separated by single newline chars, so we can use that to delineate between them
        if passport == "\n" or i == len(unformatted_passports):
            passport_map = {}

            #Passport key:value pairs are separated by spaces, so we can use a space as the spot to split
            for entry in formatted_passport[:-1].split(" "):

                #Passport data is in the form key:value, so find the colon & add to the dictionary using this info
                colon = formatted_passport.find(":")
                passport_map[entry[:colon]] = entry[colon + 1:]

            passports.append(passport_map)
            formatted_passport = ""

        #f.readlines() adds a \n to some passport entries.  This removes these \n.
        #Adds a space to the last entry (IE the string becomes "a: 123 b: 123_" which is handled using [:-1] above
        else:
            formatted_passport += passport.replace("\n", " ")

    return passports

#Lots of if statements to check if various criteria are met.  Not very exciting or important.
def check_data(passport):
    for key in passport.keys():
        try:
            if key == "byr" and not (1920 <= int(passport[key]) <= 2002):
                return 0

            if key == "iyr" and not (2010 <= int(passport[key]) <= 2020):
                return 0

            if key == "eyr" and not (2020 <= int(passport[key]) <= 2030):
                return 0

            if key == "hgt":
                if passport[key].find("cm") != -1 and not (150 <= int(passport[key][:passport[key].find("cm")]) <= 193):
                    return 0
                if passport[key].find("in") != -1 and not (59 <= int(passport[key][:passport[key].find("in")]) <= 76):
                    return 0

            if key == "hcl":
                if passport[key][0] != "#":
                    return 0

                valid_char = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'}

                if not (set(passport[key][1:]).issubset(valid_char)) or len(passport[key][1:]) != 6:
                    return 0

            if key == "ecl":
                valid_char = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

                if not (passport[key] in valid_char):
                    return 0

            if key == "pid":
                int(passport[key])
                if len(passport[key]) != 9:
                    return 0

        except (AttributeError, ValueError):
            return 0

    return 1


def check_passports():
    passports = get_passports()
    required_fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
    valid_passports_pt1 = 0
    valid_passports_pt2 = 0

    for passport in passports:

        #Checks if the passport is valid using set(Required) - set(Passport.keys) difference
        #We don't care if the passport has extra data, just that it has the required values; hence required - keys
        diff = set(required_fields) - set(passport.keys())

        #If req - keys == empty set, then keys has all fields in required and we count as valid
        if diff == set():
            valid_passports_pt1 += 1

            #After checking if all fields are present, validate the data in those fields.
            valid_passports_pt2 += check_data(passport)

    return valid_passports_pt1, valid_passports_pt2


answer = check_passports()
print(f"Part1: {answer[0]}\nPart2: {answer[1]}")
