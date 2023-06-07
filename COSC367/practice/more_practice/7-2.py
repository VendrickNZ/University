def n_queens_cost(state):
    total = 0
    for i in range(len(state)):
        for j in range(i+1, len(state)):
            dx, dy = j-i, state[i]-state[j]
            if abs(dx) == abs(dy) and (dx and dy) != 0:
                total += 1
    return total