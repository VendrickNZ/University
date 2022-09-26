
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




# It should also work undirected graphs.
# The output will be the same as input.

# graph_string = """\
# U 7
# 1 2
# 1 5
# 1 6
# 2 3
# 2 5
# 3 4
# 4 5
# """

# graph_adj_list = adjacency_list(graph_string)
# graph_transposed_adj_list = transpose(graph_adj_list)
# for i in range(len(graph_transposed_adj_list)):
#     print(i, sorted(graph_transposed_adj_list[i]))