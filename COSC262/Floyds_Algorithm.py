from math import inf
import pprint

def floyd(distance):
    n = len(distance)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
    return distance

def distance_matrix(adj_list):
    n = len(adj_list)
    distance = [[inf for i in range(n)] for j in range(n)]
    for i in range(len(distance)):
        for j in range(len(adj_list[i])):
            distance[i][adj_list[i][j][0]] = adj_list[i][j][1]
    for i in range(len(distance)):
        distance[i][i] = 0
    return distance

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

# import pprint

# graph_str = """\
# U 7 W
# 0 1 5
# 0 2 7
# 0 3 12
# 1 2 9
# 2 3 4
# 1 4 7
# 2 4 4
# 2 5 3
# 3 5 7
# 4 5 2
# 4 6 5
# 5 6 2
# """

# pprint.pprint(floyd(distance_matrix(adjacency_list(graph_str))))