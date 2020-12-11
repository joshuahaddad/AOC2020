def check_seat(x, y, seats, occupied_criteria):
    seat_state = seats[y][x]
    connected_seats = []
    dseat = 1

    #Get Horizontals, Verticals, and Diagonals
    if x + dseat < len(seats[y]):
        connected_seats.append(seats[y][x+dseat])
    if x-dseat >= 0:
        connected_seats.append(seats[y][x-dseat])

    #Verticals
    if y+dseat < len(seats) and x < len(seats[y+dseat]):
        connected_seats.append(seats[y+dseat][x])
    if y-dseat >= 0:
        connected_seats.append(seats[y-dseat][x])

    #Diagonals
    if y+dseat < len(seats) and x+dseat < len(seats[y+dseat]):
        connected_seats.append(seats[y+dseat][x+dseat])
    if x-dseat >= 0 and y-dseat >= 0:
        connected_seats.append(seats[y-dseat][x-dseat])
    if x-dseat >= 0 and y+dseat < len(seats):
        connected_seats.append(seats[y+dseat][x-dseat])
    if y-dseat >= 0 and x+dseat < len(seats[y-dseat]):
        connected_seats.append(seats[y-dseat][x+dseat])

    if seat_state == "L" and connected_seats.count("#") == 0:
        return "#"
    elif seat_state == "#" and connected_seats.count("#") >= occupied_criteria:
        return "L"
    else:
        return seat_state