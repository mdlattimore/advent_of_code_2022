# All the heavy lifting in this one is done in the data file where the instructions are converted into a usable form -- a lists of lists containing 3 ints: The number of items to be moved, the stack from which the item(s) are to be moved, and the stack to where the item(s) are to be moved.
from day5_data import scrubbed_data

# Starting stacks. Lists are perfect as they are LIFO stacks

one = "Q M G C L".split()
two = "R D L C T F H G".split()
three = "V J F N M T W R".split()
four = "J F D V Q P".split()
five = "N F M S L B T".split()
six = "R N V H C D P".split()
seven = "H C T".split()
eight = "G S J V Z N H P".split()
nine = "Z F H G".split()

# I have included an empty list at index position 0 so the index positions will match the ints in the move instructions--starting at 1. It's easier than adding '+ 1' to every index.
stacks = [[], one, two, three, four, five, six, seven, eight, nine]

move_num = 0
for move in scrubbed_data:
    for i in range(move[0]):
        a = stacks[move[1]].pop()
        stacks[move[2]].append(a)

    # Diagnostic    
        # print()
    # move_num += 1
    # for stack in stacks:
    #     print(stack)
    # print(move_num)

# Part 1 Solution
for n in stacks[1:]:  # Start at index position 1 to skip the empty placeholder list at 0
    print(n[-1])






