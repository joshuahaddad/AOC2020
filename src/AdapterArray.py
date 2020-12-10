# Day 10 Adapter Array

#Gets the sorted jolt values from the problem input and adds the beginning 0 & the device "built-in" adapter jolts
def get_jolts():
    with open("../assets/test.txt", 'r') as f:
        jolts = [int(line) for line in f.readlines()]
        jolts.append(0)
        jolts.sort()
        jolts.append(jolts[len(jolts) - 1] + 3)
    return jolts


def get_dV():
    jolts = get_jolts()
    current_jolt = jolts[0]
    dV = []

    #Jolts are sorted, so check if the next jolt is within 1,2,3 jolts.
    #Add dVs to list & return if end of jolts/condition not met
    for jolt in jolts:

        if jolt == 0:
            continue

        if current_jolt < jolt <= current_jolt + 3:
            dV.append(jolt - current_jolt)
            current_jolt = jolt
        else:
            break
    return (dV.count(1) * dV.count(3))


# Counts the number of arrangements by generating a graph and counting the paths from vertex 0 to vertex max(jolts)
def get_arrangements():
    graph = {}
    jolts = get_jolts()

    #Build jolt graph with vertex = jolt, edges = connections to other jolts: {jolt: [connected jolts]}
    for jolt in jolts:
        graph[jolt] = []

        for i in range(1, 4):
            if jolt + i in jolts:
                graph[jolt].append(jolt + i)

    start = 0
    end = jolts[len(jolts) - 1]

    return count_paths(start, end, graph, {})


# Calculates the total number of paths in the acyclic graph from a start point to an end point
def count_paths(start, end, graph, visited_nodes):
    count = 0

    # End of path condition, add one
    if start == end:
        return count + 1

    for path in graph[start]:

        # If we have already calculated the path length of a particular jolt, do not recalculate
        if path in visited_nodes:
            count += visited_nodes[path]
            continue

        # Count the number of paths from each of the options in the current path
        count += count_paths(path, end, graph, visited_nodes)

    # Add the node to a visited nodes dictionary for use later
    visited_nodes[start] = count

    return count


print(f"Part1: {get_dV()} \nPart2: {get_arrangements()}")
