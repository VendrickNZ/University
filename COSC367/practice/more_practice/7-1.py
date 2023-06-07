def n_queens_neighbours(state):
    returned_list = []
    for i in range(len(state)):
        for j in range(i+1, len(state)):
            state_list = list(state)
            state_list[i], state_list[j] = state_list[j], state_list[i]
            returned_list.append(tuple(state_list))
    return sorted(returned_list)