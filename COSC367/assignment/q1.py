from search import *
import math
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

def main():
    
    map_str = """\
    +-------+
    |P 9  XG|
    |X SXX P|
    | S  0FG|
    |XP P XX|
    +-------+
    """

    graph = RoutingGraph(map_str)

    print("Starting nodes:", sorted(graph.starting_nodes()))
    print("Outgoing arcs (available actions) at starting states:")
    for s in sorted(graph.starting_nodes()):
        print(s)
        for arc in graph.outgoing_arcs(s):
            print ("  " + str(arc))

    node = (1,1,5)
    print("\nIs {} goal?".format(node), graph.is_goal(node))
    print("Outgoing arcs (available actions) at {}:".format(node))
    for arc in graph.outgoing_arcs(node):
        print ("  " + str(arc))

    node = (1,7,2)
    print("\nIs {} goal?".format(node), graph.is_goal(node))
    print("Outgoing arcs (available actions) at {}:".format(node))
    for arc in graph.outgoing_arcs(node):
        print ("  " + str(arc))

    node = (3, 7, 0)
    print("\nIs {} goal?".format(node), graph.is_goal(node))

    node = (3, 7, math.inf)
    print("\nIs {} goal?".format(node), graph.is_goal(node))

    node = (3, 6, 5)
    print("\nIs {} goal?".format(node), graph.is_goal(node))
    print("Outgoing arcs (available actions) at {}:".format(node))
    for arc in graph.outgoing_arcs(node):
        print ("  " + str(arc))

    node = (3, 6, 9)
    print("\nIs {} goal?".format(node), graph.is_goal(node))
    print("Outgoing arcs (available actions) at {}:".format(node))
    for arc in graph.outgoing_arcs(node):
        print ("  " + str(arc))

    node = (2, 7, 4)  # at a location with a portal
    print("\nOutgoing arcs (available actions) at {}:".format(node))
    for arc in graph.outgoing_arcs(node):
        print ("  " + str(arc))


if __name__ == "__main__":
    main()
