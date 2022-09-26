from collections import deque

def dfs_tree(adj_list, start):
    n = len(adj_list)
    state = []
    parent_array = []
    for i in range(n):
        state.append("U")
        parent_array.append(None)
    state[start] = "D"

    dfs_loop(adj_list, start, state, parent_array)

    return parent_array

def dfs_loop(adj_list, start, state, parent_array):
    for v in adj_list[start]:
        neighbour = v[0]
        if state[neighbour] == "U":
            state[neighbour] = "D"
            parent_array[neighbour] = start
            dfs_loop(adj_list, neighbour, state, parent_array)
        state[start] = "P"

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
D 5
4 0
1 3
1 2
3 4
"""

adj_list = adjacency_list(graph_string)

print(dfs_tree(adj_list, 4))

# adj_list = [
#     [(1, None), (2, None)],
#     [(0, None), (2, None)],
#     [(0, None), (1, None)]
# ]

# print(dfs_tree(adj_list, 0))
# print(dfs_tree(adj_list, 1))
# print(dfs_tree(adj_list, 2))