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
    
    def add(self, path):
        heuristic = self.map_graph.estimated_cost_to_goal(path[-1][0])
        total_path_cost = 0
        for arc in path:
            total_path_cost += arc.cost
        if path[-1] not in self.expanded_nodes:
            heapq.heappush(self.container, (total_path_cost + heuristic, self.count, path))
            self.count += 1
            self.expanded_nodes.add(path[-1])

    def __iter__(self):
        while self.container:
            yield heapq.heappop(self.container)[-1]
            

    def __next__(self):
        return 0

#no pruning
#

def main():
    
    map_str = """\
    +-------+
    |   G   |
    |       |
    |   S   |
    +-------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)

    map_str = """\
    +-------+
    |  GG   |
    |S    G |
    |  S    |
    +-------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)

    map_str = """\
    +-------+
    |     XG|
    |X XXX  |
    | S     |
    +-------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)

    
    map_str = """\
    +-------+
    |  F  X |
    |X XXXXG|
    | 3     |
    +-------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)

    map_str = """\
    +--+
    |GS|
    +--+
    """
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)

    map_str = """\
    +---+
    |GF2|
    +---+
    """
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)

    map_str = """\
    +----+
    | S  |
    | SX |
    |GX G|
    +----+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)

    map_str = """\
    +---------+
    |         |
    |    G    |
    |         |
    +---------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)

    
    map_str = """\
    +----------+
    |    X     |
    | S  X  G  |
    |    X     |
    +----------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)
if __name__ == "__main__":
    main()