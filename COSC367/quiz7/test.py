a = [1, 2, 3, 4, 5]
for i in range(len(a)):
    print(i)

def greedy_descent_with_random_restart(random_state, neighbours, cost) -> list:
    min_state = random_state()
    reached_min = False
    min_neighbour = None

    while not reached_min:
        print(min_state)
        neighbors = neighbours(min_state)
        if len(neighbors) == 0:
            neighbors = [min_state]
        min_neighbour = min(neighbors, key=cost)
        min_neighbour_cost = cost(min_neighbour)
        min_state_cost = cost(min_state)
        if min_neighbour_cost < min_state_cost:
            min_state = min_neighbour
        elif min_state_cost == 0:
            reached_min = True
        else:
            print('RESTART')
            min_state = random_state()


    # def greedy_descent_with_random_restart(random_state, neighbours, cost):
    # lowest_cost = math.inf
    # best_state = None
    # global_min = False
    # while not global_min:
    #     current_random_state = random_state()
    #     print(current_random_state)
    #     random_state_cost = cost(current_random_state)
    #     random_state_neighbours = neighbours(current_random_state)
    #     for state in random_state_neighbours:
    #         if cost(state) < lowest_cost:
    #             lowest_cost = cost(state)
    #             best_state = state
    #     if random_state_cost == 0:
    #         global_min = True
    #     else:
    #         print("RESTART")