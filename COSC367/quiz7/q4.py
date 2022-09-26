import random
import math
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
def n_queens_cost(state):
    total = 0
    for i in range(len(state)):
        for j in range(i+1, len(state)):
            dx, dy = j - i, state[j] - state[i]
            if (abs(dx) == abs(dy)) and (dx and dy) != 0:
                total+=1
    return total
def n_queens_neighbours(state):
    returned_list = []
    for i in range(len(state)):
        for j in range(i+1, len(state)):
            state_list = list(state)
            state_list[i], state_list[j] = state[j], state[i]
            returned_list.append(tuple(state_list))
    return sorted(returned_list)

def greedy_descent_with_random_restart(random_state, neighbours, cost):
    global_min = False
    new_random_state = random_state()

    while not global_min:
        best_state = None
        lowest_cost = math.inf
        print(new_random_state)
        random_state_neighbours = neighbours(new_random_state)
        random_state_cost = cost(new_random_state)
        for state in random_state_neighbours:
            if cost(state) < lowest_cost:
                lowest_cost = cost(state)
                best_state = state
        #print(lowest_cost, random_state_cost, new_random_state)
        if lowest_cost < random_state_cost:
            new_random_state = best_state
        elif random_state_cost == 0:
            global_min = True
        else:
            print("RESTART")
            new_random_state = random_state()


if __name__ == "__main__":
    N = 6
    random.seed(0)

    def random_state():
        return tuple(random.sample(range(1,N+1), N))   
    greedy_descent_with_random_restart(random_state, n_queens_neighbours, n_queens_cost)
