#Day 12 Rain Risk

#Making an object for this challenge seemed appropriate as I expected pt2 to have multiple boats :)
class Boat:

    #Boat has a position x/y, a current direction (in the form of an int) and possible directions
    def __init__(self, x, y, direction=0):
        self.x = x
        self.y = y
        self.directions = ["N", "E", "S", "W"]
        self.direction = direction


    #Changes the direction of the boat.  The problem only had directions in the cardinal directions
    #If the problem statement wanted to handle non-cardinal directions, boat.direction would be in degrees instead of an int 0-3
    def rotate(self, rot, degrees):
        rot = 1 if rot == "R" else -1
        self.direction = int((self.direction + rot*degrees / 90) % 4)

    #Rotate function for the waypoint (IE rotating a boat object that is not in the main reference frame)
    def rotate_waypoint(self, rot, degrees):

        #How many iterations to rotate (0 --> 0, 90 --> 1, 180 --> 2, 270 --> 3, 360 --> 0)
        rotations = (degrees / 90) % 4

        #If rotating counterclockwise, we take the corresponding clockwise rotation:
        #0 deg cw --> 0 deg ccw, 90 deg cw --> 270 deg ccw, 180 deg cw --> 180 deg ccw, 270 deg cw --> 90 deg ccw
        if rot == "L":
            rotations = (4 - rotations) % 4

        #Rotate the coordinates rotations number of times.  A rotation is (x, y) --> (y, -x) in this coordinate system
        for _ in range(int(rotations)):
            temp = self.x
            self.x = self.y
            self.y = -temp

    #Moves a boat object in a specified direction or in the current direction of the boat by "distance" units
    def move(self, direction, distance):
        if direction == "N":
            self.y += distance
        elif direction == "S":
            self.y -= distance
        elif direction == "E":
            self.x += distance
        elif direction == "W":
            self.x -= distance
        else:
            #Move the boat in the direction that it currently faces
            self.move(self.directions[self.direction], distance)

    #Gets manhattan distance (rectangular distance) of a boat's position and a given starting position (0,0) default
    def get_manhattan(self, x1=0, y1=0):
        return abs(self.x-x1)+abs(self.y-y1)

#Gets the problem movement commands in the form of tuples (string command, int value)
def get_movements():
    with open("../assets/shipmovement.txt", 'r') as f:
        return [(line[0], int(line[1:-1])) for line in f.readlines()]

#Executes the movements with the ruleset given in part 1
def exec_movements():
    boat = Boat(0,0,1)
    movements = get_movements()
    for movement in movements:
        if movement[0] == "L" or movement[0] == "R":
            boat.rotate(movement[0], movement[1])
        else:
            boat.move(movement[0], movement[1])

    return boat.get_manhattan()

#Executes the movement with the ruleset given in part 2
def exec_movements_waypoint():
    boat = Boat(0,0,1)
    waypoint = Boat(10,1,1)
    movements = get_movements()

    for movement in movements:
        if movement[0] == "R" or movement[0] == "L":
            waypoint.rotate_waypoint(movement[0], movement[1])
        elif movement[0] == "F":
            boat.x += waypoint.x * movement[1]
            boat.y += waypoint.y * movement[1]
        else:
            waypoint.move(movement[0], movement[1])

    return boat.get_manhattan()

print(f'Part1: {exec_movements()}\nPart2: {exec_movements_waypoint()}')
