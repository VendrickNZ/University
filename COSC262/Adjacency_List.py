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


# graph_str = """\
# U 17
# 1 2
# 1 15
# 1 6
# 12 13
# 2 15
# 13 4
# 4 5
# """

# print(adjacency_list(graph_str))