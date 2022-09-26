def dfs_tree(adj_list, start):
    n = len(adj_list)
    state = []
    parent_array = []
    result = []
    for i in range(n):
        state.append("U")
        parent_array.append(None)
    state[start] = "D"

    dfs_loop(adj_list, start, state, parent_array, result)
    print(state[0:])
    return result


def dfs_loop(adj_list, start, state, parent_array, result):
    for v in adj_list[start]:
        neighbour = v[0]
        if state[neighbour] == "U":
            state[neighbour] = "D"
            parent_array[neighbour] = start
            dfs_loop(adj_list, neighbour, state, parent_array, result)
        state[start] = "P"
        result.append(neighbour)



def adjacency_list(graph_str):
    graph_split = graph_str.splitlines()
    split_two = graph_split[0].split(" ")
    result = []
    is_direct = False

    for i in range(0, int(split_two[1])):
        result.append([])

    if split_two[0] == "D":
        is_direct = True

    for num in range(1, len(graph_split)):
        split_more = graph_split[num].split(" ")
        if len (split_more) < 3:
            stuff = None
        else:
            stuff = int(split_more[2])
    
        result[int(split_more[0])].append((int(split_more[1]), stuff))
        
        if not is_direct:
            result[int(split_more[1])].append((int(split_more[0]), stuff))
    return result

# graph from the textbook example
graph_string = """\
D 4
0 3
"""

for i in range(len(adjacency_list(graph_string))):
    print(dfs_tree(adjacency_list(graph_string), i))