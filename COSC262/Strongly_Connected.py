def is_strongly_connected(adj_list):
    vertex_state = dfs_tree(adj_list, 0)
    graph_transpose = transpose(adj_list)
    transpose_state = dfs_tree(graph_transpose, 0)
    if transpose_state and vertex_state == True:
        return True
    else:
        return False
def dfs_tree(adj_list, start):
    n = len(adj_list)
    state = []
    parent_array = []
    for i in range(n):
        state.append("U")
        parent_array.append(None)
    state[start] = "D"

    dfs_loop(adj_list, start, state, parent_array)
    vertex_state = True
    for i in range(n):
        if state[i] == "U":
            vertex_state = False
    return vertex_state
def dfs_loop(adj_list, start, state, parent_array):
    for v in adj_list[start]:
        neighbour = v[0]
        if state[neighbour] == "U":
            state[neighbour] = "D"
            parent_array[neighbour] = start
            dfs_loop(adj_list, neighbour, state, parent_array)
        state[start] = "P"



def transpose(adj_list):
    n = len(adj_list)
    result = [[] for i in range(n)]
    
    for i in range(n):
        if len(adj_list[i]) > 1:
            for tup in adj_list[i]:
                result[tup[0]].append((i, tup[1]))
        else:
            if len(adj_list[i]) == 0:
                continue
            else:
                result[adj_list[i][0][0]].append((i, adj_list[i][0][1]))
    return result



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


# graph_string = """\
# U 5
# 2 4
# 3 1
# 0 4
# 2 1
# """

# print(is_strongly_connected(adjacency_list(graph_string)))