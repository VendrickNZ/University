def is_solution(candidate, input_data):
    """Returns True if the candidate is complete solution"""
    return len(candidate) == len(input_data)


def children(candidate, input_data):

    input_list = list(input_data)
    perm_list = []

    if len(input_data) == 1:
        return [tuple(input_data)]
    
    for index in range(len(input_data)):
        item = input_list[index]

        candidate = input_list[:index] + input_list[index+1:]

        for items in children((), candidate):
            perm_list.append(tuple([item]) + tuple(items))
    return perm_list

def permutations(s):
    solutions = []
    dfs_backtrack((), s, solutions)
    return solutions


def dfs_backtrack(candidate, input_data, output_data):
    if should_prune(candidate):
        return
    if is_solution(candidate, input_data):
        add_to_output(candidate, output_data)
    else:
        for child_candidate in children(candidate, input_data):
            dfs_backtrack(child_candidate, input_data, output_data)

    
def add_to_output(candidate, output_data):
    output_data.append(candidate)

    
def should_prune(candidate):
    return False

print(sorted(permutations({1,2,3})))



