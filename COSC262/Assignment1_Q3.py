import Adjacency_List
import Topological_Sorting

def build_order(dependencies):
    adj_list = Adjacency_List.adjacency_list(dependencies)
    Topological_Sorting.dfs_tree(adj_list, )

    #topological sorting


dependencies = """\
D 2
0 1
"""

print(build_order(dependencies))