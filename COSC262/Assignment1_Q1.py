def format_sequence(converters_info, source_format, destination_format):
    """converters_info is the adjacency list
    source_format is the starting vertex
    destination_format is the destination vertex"""
    
    #backtracking


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


converters_info_str = """\
D 2
0 1
"""

source_format = 0
destination_format = 1

converter_adj_list = adjacency_list(converters_info_str)
print(converter_adj_list)
