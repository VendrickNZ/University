def max_value(tree):
    largest=0
    if not isinstance(tree, list):
        return tree
    else:
        for child in tree:
            if min_value(child) > largest:
                largest = min_value(child)
    return largest

def min_value(tree):
    if not isinstance(tree, list):
        return tree
    else:
        return min(max_value(child) for child in tree)


game_tree = 3


print("Root utility for minimiser:", min_value(game_tree))
print("Root utility for maximiser:", max_value(game_tree))