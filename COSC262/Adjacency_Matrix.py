from pprint import pprint
def adjacency_matrix(graph_str):
    graph_split = graph_str.splitlines()
    split_two = graph_split[0].split(" ")
    n = int(split_two[1])
    is_direct = False

    try:
        if split_two[2] == "W":
            matrix = [[None for i in range(n)] for j in range(n)]
        else:
            matrix = [[0 for i in range(n)] for j in range(n)]
    except:
        matrix = [[0 for i in range (n)] for j in range(n)]


    if split_two[0] == "D":
        is_direct = True
    if is_direct == True:
        for i in range(1, len(graph_split)):
            split_more = graph_split[i].split(" ")
            if len (split_more) < 3:
                stuff = None
            else:
                stuff = int(split_more[2])
            if stuff != None:
                (matrix[int(split_more[0])][int(split_more[1])]) = stuff
            else:
                (matrix[int(split_more[0])][int(split_more[1])]) = 1
    else:
        for i in range(1, len(graph_split)):
            split_more = graph_split[i].split(" ")
            if len (split_more) < 3:
                stuff = None
            else:
                stuff = int(split_more[2])
            if stuff != None:
                (matrix[int(split_more[0])][int(split_more[1])]) = stuff
                (matrix[int(split_more[1])][int(split_more[0])]) = stuff
            else:
                (matrix[int(split_more[0])][int(split_more[1])]) = 1
                (matrix[int(split_more[1])][int(split_more[0])]) = 1



    return matrix