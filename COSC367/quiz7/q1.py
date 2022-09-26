import itertools
# def n_queens_neighbours(state):
#     state_list = []
#     n = len(state)
#     for x, y in itertools.combinations(range(n), 2):
#         state = list(state)
#         state[x], state[y] = state[y], state[x]
#         state = tuple(state)
#         state_list.append(state)
#     return state_list

def n_queens_neighbours(state):
    returned_list = []
    for i in range(len(state)):
        for j in range(i+1, len(state)):
            state_list = list(state)
            state_list[i], state_list[j] = state[j], state[i]
            returned_list.append(tuple(state_list))
    return sorted(returned_list)


def main():
    print(n_queens_neighbours((1, 2)))
    print(n_queens_neighbours((1, 3, 2)))
    print(n_queens_neighbours((1, 2, 3)))
    print(n_queens_neighbours((1,)))
    # for neighbour in n_queens_neighbours((1, 2, 3, 4, 5, 6, 7, 8)):
    #     print(neighbour)
    # for neighbour in n_queens_neighbours((2, 3, 1, 4)):
    #     print(neighbour)

if __name__ == "__main__":
    main()