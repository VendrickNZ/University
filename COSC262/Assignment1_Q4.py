import Prims_Algorithm
import Adjacency_List

def which_segments(city_map):
    result = []
    adj_list = Adjacency_List.adjacency_list(city_map)
    monkey = Prims_Algorithm.prim(adj_list, 0)
    
    return monkey

"""all you do is run through the city map with prims algorithm and return every road segment
    that needs to be cleared (has a weight) so that there is a clear path between any two locations
    and the total length of the cleaned up road segments is minimised
"""

# floyds algorithm



city_map = """\
U 3 W
0 1 1
2 1 2
2 0 4
"""

print(sorted(which_segments(city_map)))