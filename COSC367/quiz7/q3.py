def greedy_descent(initial_state, neighbours, cost):
    all_states = [initial_state]
    while True:
        lowest_cost = cost(all_states[-1])
        best_state = all_states[-1]
        for state in neighbours(all_states[-1]):
            #print(state, all_states[-1])
            if cost(state) < lowest_cost:
                lowest_cost = cost(state)
                best_state = state
        if best_state == all_states[-1]:
                break
        else:
            all_states.append(best_state)
    return all_states

if __name__ == "__main__":
    def cost(x):
        return x**2

    def neighbours(x):
        return [x - 1, x + 1]

    for state in greedy_descent(4, neighbours, cost):
        print(state)
    
    for state in greedy_descent(-6.75, neighbours, cost):
        print(state)

    
    def cost(x):
        return x**2

    def neighbours(x):
        return [x - 1, x + 1, x - 2, x + 2]

    for state in greedy_descent(-6.75, neighbours, cost):
        print(state)