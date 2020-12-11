#Day 11 Seating System
import copy

def get_seats():
    with open("../assets/seats.txt", 'r') as f:
        return [list(line[:-1]) for line in f.readlines()]

def play_round(seats, occupied_criteria, part):
    new_seats = copy.deepcopy(seats)
    for y in range(len(seats)):
        for x in range(len(seats[y])):
            if part == 1:
                new_seats[y][x] = check_seat(x, y, seats, occupied_criteria)
            if part == 2:
                new_seats[y][x] = check_seat_pt2(x, y, seats, occupied_criteria)
    return new_seats

def check_exists(x, y, seats):
    try:
        seats[y][x]
    except IndexError:
        return False
    return True

def check_seat(x, y, seats, occupied_criteria):
    seat_state = seats[y][x]
    connected_seats = []
    dseat = 1

    #Get Horizontals, Verticals, and Diagonals
    if check_exists(x+dseat, y, seats):
        connected_seats.append(seats[y][x+dseat])

    if check_exists(x-dseat, y, seats) and x-dseat >= 0:
        connected_seats.append(seats[y][x-dseat])

    #Verticals
    if check_exists(x, y+dseat, seats):
        connected_seats.append(seats[y+dseat][x])
    if check_exists(x, y-dseat, seats) and y-dseat >= 0:
        connected_seats.append(seats[y-dseat][x])

    #Diagonals
    if check_exists(x+dseat, y+dseat, seats):
        connected_seats.append(seats[y+dseat][x+dseat])

    if check_exists(x-dseat, y-dseat, seats) and y-dseat >= 0 and x-dseat >= 0:
        connected_seats.append(seats[y-dseat][x-dseat])

    if check_exists(x-dseat, y+dseat, seats) and x-dseat >= 0:
        connected_seats.append(seats[y+dseat][x-dseat])

    if check_exists(x+dseat, y-dseat, seats) and y-dseat >= 0:
        connected_seats.append(seats[y-dseat][x+dseat])

    if seat_state == "L" and connected_seats.count("#") == 0:
        return "#"
    elif seat_state == "#" and connected_seats.count("#") >= occupied_criteria:
        return "L"
    else:
        return seat_state

def check_seat_pt2(x, y, seats, occupied_criteria):
    seat_state = seats[y][x]
    connected_seats = []
    dseat = 1

    #Get Horizontals, Verticals, and Diagonals
    if check_exists(x+dseat, y, seats):
        while seats[y][x+dseat] == "." and check_exists(x+dseat+1, y, seats):
            dseat += 1
        connected_seats.append(seats[y][x+dseat])
        dseat = 1

    if check_exists(x-dseat, y, seats) and x-dseat >= 0:
        while seats[y][x-dseat] == "." and check_exists(x-dseat-1, y, seats) and x-dseat-1>=0:
            dseat += 1
        connected_seats.append(seats[y][x-dseat])
        dseat = 1

    #Verticals
    if check_exists(x, y+dseat, seats):
        while seats[y+dseat][x] == "." and check_exists(x, y+dseat+1, seats):
            dseat += 1
        connected_seats.append(seats[y+dseat][x])
        dseat = 1

    if check_exists(x, y-dseat, seats) and y-dseat >= 0:
        while seats[y-dseat][x] == "." and check_exists(x, y-dseat-1, seats) and y - dseat-1 >=0:
            dseat += 1
        connected_seats.append(seats[y-dseat][x])
        dseat = 1

    #Diagonals
    if check_exists(x+dseat, y+dseat, seats):
        while seats[y+dseat][x+dseat] == "." and check_exists(x+dseat+1, y+dseat+1, seats):
            dseat += 1
        connected_seats.append(seats[y+dseat][x+dseat])
        dseat = 1

    if check_exists(x-dseat, y-dseat, seats) and y-dseat >= 0 and x-dseat >= 0:
        while seats[y - dseat][x - dseat] == "." and check_exists(x - dseat - 1, y - dseat - 1, seats) and y-dseat-1 >= 0 and x-dseat-1 >= 0:
            dseat += 1
        connected_seats.append(seats[y-dseat][x-dseat])
        dseat = 1

    if check_exists(x-dseat, y+dseat, seats) and x-dseat >= 0:
        while seats[y + dseat][x - dseat] == "." and check_exists(x - dseat - 1, y + dseat + 1, seats) and x-dseat-1 >= 0:
            dseat += 1
        connected_seats.append(seats[y+dseat][x-dseat])
        dseat = 1

    if check_exists(x+dseat, y-dseat, seats) and y-dseat >= 0:
        while seats[y - dseat][x + dseat] == "." and check_exists(x + dseat + 1, y - dseat - 1, seats) and y-dseat-1 >= 0:
            dseat += 1
        connected_seats.append(seats[y-dseat][x+dseat])

    if seat_state == "L" and connected_seats.count("#") == 0:
        return "#"
    elif seat_state == "#" and connected_seats.count("#") >= occupied_criteria:
        return "L"
    else:
        return seat_state

def part1():
    seats = get_seats()
    while seats != play_round(seats, 4, 1):
        seats = play_round(seats, 4, 1)

    num_occupied = 0
    for line in seats:
        num_occupied += line.count("#")
    print(num_occupied)

def part2():
    seats = get_seats()
    while seats != play_round(seats, 5, 2):
        seats = play_round(seats, 5, 2)


    num_occupied = 0
    for line in seats:
        num_occupied += line.count("#")
    print(num_occupied)


part1()
part2()


