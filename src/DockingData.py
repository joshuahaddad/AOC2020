from copy import deepcopy

#Permutation helper code to find all strings of length k with characters ['0', '1']
#Inspired by https://www.geeksforgeeks.org/print-all-combinations-of-given-length/
def get_permutations(k):
    n = 2
    combos = []
    permutations_recursive(["0", "1"], "", n, k, combos)
    return combos


def permutations_recursive(options, prefix, n, k, combos):
    if k == 0:
        combos.append(list(prefix))
        return

    for i in range(n):
        new_prefix = prefix + options[i]
        permutations_recursive(options, new_prefix, n, k - 1, combos)

#Gets the masks and instructions in a workable format.  masks[i] corresponds to instructions[i] = [instr 1, instr2, ...]
def get_program():
    masks = []
    instructions = []

    #Start at i = -1 as the text format goes mask --> instructions --> new mask
    i = -1
    with open("../assets/bitmask.txt", 'r') as f:
        for line in f.readlines():

            #If a mask is found, increment i, add an empty array to instructions (to hold an array of instructions)
            if "mask" in line:
                i += 1
                instructions.append([])
                masks.append(line[7:-1])

            #If an instruction is found, add this instruction to the corresponding mask's instruction array
            if "mem" in line:
                instructions[i].append((int(line[4:line.index("]")]), int(line[line.index("=") + 2:])))
        f.close()

    return masks, instructions


def apply_mask(mask, value, pt):

    #Convert decimal int to binary string and add padding 0s, convert this and mask to a char array
    binary = "{0:b}".format(value)
    binary = list("0" * (36 - len(binary)) + binary)
    mask = list(mask)

    #For each byte, modify if needed depending on the ruleset (pt1/2)
    for i in range(36):

        #Both parts always write 1 if the mask has a value of 1
        if mask[i] == '1':
            binary[i] = mask[i]

        #Part 2 does not overwrite the value if the mask has a value of 0, part 1 does
        if mask[i] == '0':
            if pt == 1:
                binary[i] = mask[i]

        #Part 1 ignores the X values in the mask, Part 2 treats them as floating numbers that can be either 0/1
        if pt == 2 and mask[i] == 'X':
            binary[i] = mask[i]

    #Part 2 returns an array of mem addresses, unlike part 1 which returns a decimal int
    if pt == 2:
        mem_list = []
        # Get all combos for the num of floating X we have. Each sub-array will specify the value of the ith "X"
        # For example ['0', '1'] would assign the first 'X' to 0 and the second to '1'
        combos = get_permutations(binary.count("X"))

        # Get the indeces of each "X" in the binary
        X_idx = [j for j, x in enumerate(binary) if x == "X"]

        # For each combo, create a new binary, replace the X values, and add it to the overall mem list
        for combo in combos:
            new_binary = deepcopy(binary)

            i = 0
            for x_idx in X_idx:
                new_binary[x_idx] = combo[i]
                i += 1

            #Add the calculated memory address to a total list to be returned
            mem_list.append(int("".join(new_binary), 2))

        #Return the memory addresses to be modified
        return mem_list

    #Part 1 takes the masked value and uses the decimal version
    return int("".join(binary), 2)


def exec_instructions(pt):
    #Masks = [], instructions = [tuple(mem_address, value)]
    masks, instructions = get_program()

    #Handling the memory as a dictionary makes things easy :)
    mem = {}

    #For each mask execute each instruction corresponding to that mask
    for i in range(len(masks)):
        for instruction in instructions[i]:

            if pt == 1:
                mem[instruction[0]] = apply_mask(masks[i], instruction[1], 1)

            #Gets the addresses to be modified from the mask & modifies them to the instruction[1] value
            elif pt == 2:
                addresses = apply_mask(masks[i], instruction[0], 2)
                for address in addresses:
                    mem[address] = instruction[1]

    return sum(mem.values())

print(f"Part1: {exec_instructions(1)}\nPart2: {exec_instructions(2)}")
