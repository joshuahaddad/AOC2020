# Day 5 Binary Boarding
from math import floor, ceil

def get_boardingpasses():
    with open("../assets/planeseats.txt", 'r') as f:
        return [line[:-1] for line in f.readlines()]

#Calculates an id for a boarding pass by splicing ranges taking the upper/lower half depending on the character
def get_id(boarding_pass):
    row_lower_bound = 0
    row_upper_bound = 127

    col_lower_bound = 0
    col_upper_bound = 7

    row = 0
    col = 0

    #Simple math relation to take the upper/lower range of numbers.  row/col = last splice taken in the series
    for character in boarding_pass:
        if character == "F":
            row_upper_bound = row_lower_bound + floor((row_upper_bound - row_lower_bound) / 2)
            row = row_upper_bound
        if character == "B":
            row_lower_bound = row_lower_bound + ceil((row_upper_bound - row_lower_bound) / 2)
            row = row_lower_bound

        if character == "L":
            col_upper_bound = col_lower_bound + floor((col_upper_bound - col_lower_bound) / 2)
            col = col_upper_bound

        if character == "R":
            col_lower_bound = col_lower_bound + ceil((col_upper_bound - col_lower_bound) / 2)
            col = col_lower_bound

    return 8 * row + col

#Finds the highest id in a series of boarding passes by calculating a max
def get_highest_id():
    return max([get_id(boarding_pass) for boarding_pass in get_boardingpasses()])

#Finds "your" boarding pass IE [1,2,3,5] returns 4 since 4 is missing from the series
def find_boarding_id():
    pass_ids = [get_id(boarding_pass) for boarding_pass in get_boardingpasses()]

    #Sorting the array makes this task trivial
    pass_ids.sort()

    for i in range(len(pass_ids) - 1):
        if pass_ids[i] + 2 == pass_ids[i + 1]:
            return pass_ids[i] + 1


print(f'Part1: {get_highest_id()}\nPart2: {find_boarding_id()}')
