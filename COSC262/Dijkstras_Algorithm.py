

def dijkstra(adj_list, start):
    n = len(adj_list)
    in_tree = []
    distance = []
    parent_array = []
    
    for i in range(n):
        in_tree.append(False)
        distance.append(float('inf'))
        parent_array.append(None)

    distance[start] = 0

    print(in_tree)
    while all(in_tree) != True:
        u = next_vertex(in_tree, distance)
        in_tree[u] = True

        for v, weight in adj_list[u]:
            if not in_tree[v] and (distance[u] + weight) < distance[v]:
                distance[v] = distance[u] + weight
                parent_array[v] = u

    return parent_array, distance

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
            result[int(split_more[0])].append((int(split_more[0]), stuff))
    return result


graph_string = """\
D 3 W
1 0 3
2 0 1
1 2 1
"""

print(dijkstra(adjacency_list(graph_string), 1))
print(dijkstra(adjacency_list(graph_string), 2))
