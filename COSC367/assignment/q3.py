import math
from search import *
import heapq
class RoutingGraph(Graph):
    def __init__(self, map_str):
        self.customers, self.agents, self.fuel_stations, self.portals, self.map = self.node_finder(map_str)

    def is_goal(self, node):
        return node[0:2] in self.customers
    
    def starting_nodes(self):
        return self.agents
    
    def outgoing_arcs(self, tail_node):
        directions = [('N' , -1, 0),
                    ('E' ,  0, 1),
                    ('S' ,  1, 0),
                    ('W' ,  0, -1),]
        obstacles = ["X", "+", "-", "|"]
        self.map = [x.strip(' ') for x in self.map]
        row, col, fuel = tail_node
        if fuel > 0:
            for direction, row_dir, col_dir in directions:
                new_row, new_col = row + row_dir, col + col_dir 
                if self.map[new_row][new_col] not in obstacles:
                    head = (new_row, new_col, fuel - 1)
                    yield Arc(tail_node, head, action=direction, cost=5)
        if fuel < 9 and ((row, col)) in self.fuel_stations:
            head = (row, col, 9)
            yield Arc(tail_node, head, action="Fuel up", cost=15)
        if (row, col) in self.portals:
            for element in sorted(self.portals, key=lambda x:self.portals[0]):
                if element == (row, col):
                    continue
                head = (element[0], element[1], fuel)
                yield Arc(tail_node, head, action=f"Teleport to ({element[0]}, {element[1]})", cost=10)
    
    def estimated_cost_to_goal(self, node):
        #going to make the assumption there's only one goal node for simplicity
        goal_row, goal_col = self.customers[0][0], self.customers[0][1]
        if node:
            node_row, node_col = node[0], node[1]
            return (abs(node_row - goal_row) + abs(node_col - goal_col))
        return 0
    
    def node_finder(self, map_str):
        customers = []
        agents = []
        fuel_stations = []
        portals = []
        map_str = map_str.splitlines()
        for row_n, row in enumerate(map_str):
            row = row.strip()
            for col, element in enumerate(row):
                if element == "G":
                    customers.append((row_n, col))
                if element == "S":
                    agents.append((row_n, col, math.inf))
                if element.isdigit():
                    agents.append((row_n, col, int(element)))
                if element == "F":
                    fuel_stations.append((row_n, col))
                if element == "P":
                    portals.append((row_n, col))
        return customers, agents, fuel_stations, portals, map_str
    

class AStarFrontier(Frontier):
    def __init__(self, map_graph):
        self.container = []
        self.count = 0
        self.map_graph = map_graph
        self.expanded_nodes = set()
        self.visited = []

    def add(self, path):
        heuristic = self.map_graph.estimated_cost_to_goal(path[-1][0])
        total_path_cost = 0
        for arc in path:
            total_path_cost += arc.cost
        total_cost = heuristic + total_path_cost
        to_add = (total_cost, self.count, path)
        if path[-1] not in self.expanded_nodes:
            self.count += 1
            self.expanded_nodes.add(path[-1])
            heapq.heappush(self.container, to_add)

    def __iter__(self):
        while self.container:
            best_path = heapq.heappop(self.container)[-1]
            curr_head = best_path[-1].head
            if curr_head not in self.visited:
                self.visited.append(curr_head)
                #yield heapq.heappop(self.container)[-1]
                yield best_path
            

    def __next__(self):
        return 0




def print_map(map_graph, frontier, solution):
    solution_list = []
    for arc in solution:
        solution_list.append(arc.head)
    for i in range(len(map_graph.map)):
        to_pront = ""
        for j in range(len(map_graph.map[i])):
            if map_graph.map[i][j] == "S" or map_graph.map[i][j] == "G":
                to_pront += map_graph.map[i][j]
            elif (i, j, math.inf) in solution_list:
                to_pront += "*"
            elif (i, j, math.inf) in frontier.visited:
                to_pront += "."
            else:
                to_pront += map_graph.map[i][j]
        print(to_pront)
    #for arc in frontier.visited:
        #if arc[0] == 13:
            #print(arc)

        

    # for line in map_graph.map:
    #     to_print = ""
    #     for char in line:
    #         print(char)
    #         to_print += char
    #     if to_print:
    #         print(to_print)

def main():
    
    map_str = """\
    +----------------+                          
    |                |
    |                |
    |                |
    |                |
    |                |
    |                |
    |        S       |
    |                |
    |                |
    |     G          |
    |                |
    |                |
    |                |
    +----------------+
    """
# +----------------+
# |                |
# |                |
# |                |
# |                |
# |                |
# |                |
# |     ...S       |
# |     ...*       |
# |     ...*       |
# |     G***       |
# |                |
# |                |
# |                |
# +----------------+

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)



    # map_str = """\
    # +----------------+
    # |                |
    # |                |
    # |                |
    # |                |
    # |                |
    # |                |
    # |        S       |
    # |                |
    # |                |
    # |     G          |
    # |                |
    # |                |
    # |                |
    # +----------------+
    # """


    # map_graph = RoutingGraph(map_str)
    # # changing the heuristic so the search behaves like LCFS
    # map_graph.estimated_cost_to_goal = lambda node: 0

    # frontier = AStarFrontier(map_graph)

    # solution = next(generic_search(map_graph, frontier), None)
    # print_map(map_graph, frontier, solution)
if __name__ == "__main__":
    main()