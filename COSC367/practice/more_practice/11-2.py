def max_action_value(game_tree):
    if not isinstance(game_tree, list):
        return (None, game_tree)
    else:
        actions = [min_action_value(child)[1] for child in game_tree]
        best_action = None
        most_value = -float('inf')
        for action, value in enumerate(actions):
            if value > most_value:
                best_action = action
                most_value = value
        return (best_action, most_value)

def min_action_value(game_tree):
    if not isinstance(game_tree, list):
        return (None, game_tree)
    else:
        actions = [max_action_value(child)[1] for child in game_tree]
        best_action = None
        least_value = float('inf')
        for action, value in enumerate(actions):
            if value < least_value:
                best_action = action
                least_value = value
        return (best_action, least_value)
    

game_tree = [2, [-3, 1], 4, 1]

action, value = min_action_value(game_tree)
print("Best action if playing min:", action)
print("Best guaranteed utility:", value)
print()
action, value = max_action_value(game_tree)
print("Best action if playing max:", action)
print("Best guaranteed utility:", value)