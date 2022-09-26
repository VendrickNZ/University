import Adjacency_List
import Prims_Algorithm
def min_capacity(city_map, depot_position):
    adj_list = Adjacency_List.adjacency_list(city_map)
    prims = Prims_Algorithm.prim()
#prims algorithm?



city_map = """\
U 4 W
0 2 5
0 3 2
3 2 2
"""

print(min_capacity(city_map, 0))
print(min_capacity(city_map, 1))
print(min_capacity(city_map, 2))