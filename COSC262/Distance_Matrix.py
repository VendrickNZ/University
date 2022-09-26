from math import inf
def distance_matrix(adj_list):
    """let dist be a |V| × |V| array of minimum distances initialized to ∞ (infinity)
    for each edge (u, v) do
        dist[u][v] ← w(u, v)  // The weight of the edge (u, v)
    for each vertex v do
        dist[v][v] ← 0"""
    n = len(adj_list)
    distance = [[inf for i in range(n)] for j in range(n)]
    for i in range(len(distance)):
        distance[i][i] = 0
    for i in range(len(distance)):
        for j in range(len(adj_list[i])):
            distance[i][adj_list[i][j][0]] = adj_list[i][j][1]
    for i in range(len(distance)):
        distance[i][i] = 0
    return distance

"""Each row on a new line:
adj_list
[(1, 5)]
[(0, 5), (2, 7)]
[(1, 7)]"""






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


graph_str = """\
D 2 W
0 1 4
"""

adj_list = adjacency_list(graph_str)
print(distance_matrix(adj_list))