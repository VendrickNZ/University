BLANK = ' '

state = [[1, 2, 5],
        [3, 4, 8],
        [6, 7, 9],
        [' ', 3, 2]]

for _ in range(len(state)):
    if BLANK in state[_]:
        i = _
        j = state[i].index(BLANK)

print(i, j)