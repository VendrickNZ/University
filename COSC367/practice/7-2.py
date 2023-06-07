def cost(state):
    total = 0
    for i in range(len(state)):
        for j in range(i+1, len(state)):
            dx, dy = j - i, state[j] - state[i]
            if (abs(dx) == abs(dy) and (dx and dy) != 0):
                total+=1
    return total
print(cost((1, 2)))
print(cost((1, 3, 2)))
print(cost((1, 2, 3)))
print(cost((1,)))
print(cost((1, 2, 3, 4, 5, 6, 7, 8)))
print(cost((2, 3, 1, 4)))