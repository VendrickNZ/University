def bubbles(physical_contact_info):
    contacted_list = []
    result = []
    contact_set = set()
    adj_list = adjacency_list(physical_contact_info)
    #makes a list of things that exist
    for item in adj_list:
        if item:
            contact_list = []
            for index in range(len(item)):
                contact_set.add(item[index][0])
                contact_list.append(item[index][0])
            result.append(contact_list)
    #adds the vertices with no edges
    for items in result:
        is_duplicate = False
        if items:
            if contacted_list:
                for index in range(len(contacted_list)):
                    if contacted_list[index].count(items[0]) > 0 or contacted_list[index].count(items[1]) > 0:
                        contacted_list[index] += items
                        contacted_list[index] = list(dict.fromkeys(contacted_list[index]))
                        is_duplicate = True
                        break
                if not is_duplicate:
                    contacted_list.append(items)
                
            else:
                contacted_list.append(items)

    for num in range(int(physical_contact_info.splitlines()[0].split(" ")[1])):
        if num not in contact_set:
            contacted_list.append([num])
    return contacted_list


"""you make a new list, you see if there are any connections between the elements of the list with the adj_list and append if there is
until there are no more, and you continue until the all the elements in the adj_list have been finished """



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


physical_contact_info = """\
U 7
1 2
1 5
1 6
2 3
2 5
3 4
4 5
"""

print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))