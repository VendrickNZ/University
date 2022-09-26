from math import inf

def prim(adj_list, start):
    n = len(adj_list)
    in_tree = []
    distance = []
    parent_array = []

    for i in range(n):
        in_tree.append(False)
        distance.append(float("inf"))
        parent_array.append(None)

    distance[start] = 0

    while all(in_tree) != True:
        u = next_vertex(in_tree, distance)
        in_tree[u] = True
        for v, weight in adj_list[u]:
            if not in_tree[v] and (weight < distance[v]):
                distance[v] = weight
                parent_array[v] = u
    if len(distance) == 1:
        print(1)
        distance[0] == None
    return distance

def next_vertex(in_tree, distance):
    largest_number = float('inf')
    result = 0
    for i in range(len(in_tree)):
        if in_tree[i] == False:
            if largest_number >= distance[i]:
                largest_number = distance[i]
                result = i
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

graph_string = """\
U 1 W
"""

adj_list = adjacency_list(graph_string)

print(prim(adj_list, 0))