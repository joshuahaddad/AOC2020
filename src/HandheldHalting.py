# Day 8 HandheldHalting

"""
acc +- x = increase acc value by +- x
jmp +- x = go +- x instructions
nop = skip instruction
"""

def get_instructions():
    with open("../assets/code.txt", 'r') as f:
        #Creates instructions in form of [['acc', 5], ['jmp', -1]] and so on
        return [[line[0:3], int(line[4:])] for line in f.readlines()]

#Executes the commands in the instructions using the rules stated at the beginning of this file
def execute_instructions(instructions):
    acc = 0
    i = 0
    visited_instructions = set()

    while i < len(instructions):

        #Check if we have already visited this step
        if i in visited_instructions:
            return False, acc

        #Add current step to visited steps
        visited_instructions.add(i)

        #Execute acc/jmp commands, if nop we can just do nothing and increment i
        if instructions[i][0] == 'acc':
            acc += instructions[i][1]

        elif instructions[i][0] == 'jmp':
            i += instructions[i][1]
            continue

        i += 1

    #Used for fix_code(), if we reach this return statement the instructions executed properly
    return True, acc

#Changes one jmp/nop value in the instructions to create a valid instruction set
def fix_instructions():
    #Set initial values
    instructions = get_instructions()
    i = 0

    #Check if the instruction set is valid, if not valid remove changes & try changing next nop/jmp
    while not execute_instructions(instructions)[0]:

        #Reset the instruction set to remove previous changes as we are meant to only change 1 value
        instructions = get_instructions()

        #Find the first jmp/nop instruction by looking for values that are not 'acc'
        while instructions[i][0] == 'acc':
            i += 1

        #Change from 'nop' to 'jmp' or from 'jmp' to 'nop'
        instructions[i][0] = 'nop' if (instructions[i][0] == 'jmp') else 'jmp'

        #Increment to next step
        i += 1

    #Return the accumulator for the valid instructions & the instruction that was incorrect
    return execute_instructions(instructions)[1], i


print(f'Part1: acc = {execute_instructions(get_instructions())[1]}')
print(f'Part2: acc = {fix_instructions()[0]} by changing instruction line {fix_instructions()[1]}')
