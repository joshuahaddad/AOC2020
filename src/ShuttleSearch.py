# Day 13 Shuttle Search

from math import ceil
from math import gcd

#Exception used to find an invalid sequence of bus times (IE not x, x+1, x+2, x+3, ...) in part 2
class InvalidSequenceError(Exception):
    pass

#Text IO functions to get the data needed for each problem in each problem's convenient formatting
def get_busses():
    with open("../assets/busses.txt", 'r') as f:
        return int(f.readline()), [int(i) for i in list(filter("x".__ne__, f.readline().split(",")))]

def get_busses_pt2():
    with open("../assets/busses.txt", 'r') as f:
        f.readline()
        return f.readline().split(",")

#Gets the lcm of an array using the mathematical relation lcm(a,b) = (a*b)/gcd(a,b)
def lcm(arr):
    lcm = arr[0]
    for b in arr[1:]:
        lcm = lcm * b // gcd(lcm, b)

    return lcm

#Calculates wait times for each bus and finds the shortest wait time
def get_shortest_wait():
    time, busses = get_busses()
    wait_times = []
    for bus_time in busses:
        wait_times.append(time) if time % bus_time == 0 else wait_times.append(ceil(time / bus_time) * bus_time)
    return busses[wait_times.index(min(wait_times))] * (min(wait_times) - time)

"""
Algorithm to find the lowest time where the following is satisfied (for a general times array):
times = [t0, x1, t1, x2, x3, t2, ..., ti]
N0 = 0
Ni = Ni-1 + distance from the last t (IE N1 = 0 + 2, N2 = 2+3)
T = t0*n

Find n element of Z+ such that (T+Ni)/ti is an element of Z+ for all i

The algorithm uses the fact that once a time ti is synced, it will not desync from ti-1 if n is incremented by m*ti
As multiple times are synced, the algorithm can increment n by lcm(synced_times) to keep each number in sync

If no numbers are synced, n is incremented by 1
"""
def get_timestamp():

    #Get the bus times
    t = get_busses_pt2()

    #Construct the N array for each non-variable time entry
    N = []
    for i in range(len(t)):
        if t[i] != "x":
            t[i] = int(t[i])
            N.append(i)

    #Remove the variable x times from list as we now have the N values which represent the added distance of these x
    t = list(filter("x".__ne__, t))

    #Initialize an array for the synced_times, set n to 1, and set a flag showing a valid sequence to false
    synced_times = []
    n = 1
    valid = False

    #Loop until a valid sequence is found
    while not valid:

        #Set T using the current n
        T = t[0] * n

        #Check for a valid sequence, if an invalid sequence is found raise InvalidSequenceError
        try:
            #For each t, get the corresponding N values and check if it satisfies the problem condition
            for i in range(1, len(t)):

                #If the quotient is not a positive integer --> Invalid Sequence --> raise InvalidSequenceError
                if (T + N[i]) % t[i] != 0:
                    raise InvalidSequenceError

                #If quotient is a positive integer, add ti to synced_times if necessary,
                else:
                    if t[i] not in synced_times:
                        synced_times.append(t[i])

        #If an invalid sequence is found, increment n and try again
        except InvalidSequenceError:

            #If some numbers are synced, increment n by lcm(synced_numbers), else increment by 1
            if len(synced_times) > 0:
                n += lcm(synced_times)
            else:
                n += 1
            continue

        #If this statement is reached, the sequence is valid
        valid = True

    #Return the T value that gives a valid sequence (could also return the n if the problem wanted it)
    return T

print(f"Part1: {get_shortest_wait()}\nPart2: {get_timestamp()}")