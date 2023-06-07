from pickletools import read_stringnl_noescape_pair
import re


def neighbours(state):
    returned_list = []
    for i in range(len(state)):
        for j in range(i+1, len(state)):
            state_list = list(state)
            state_list[i], state_list[j] = state_list[j], state_list[i]
            returned_list.append(tuple(state_list))
    return returned_list



print(neighbours((1, 2)))
print(neighbours((1,)))
for neighbour in neighbours((2, 3, 1, 4)):
    print(neighbour)