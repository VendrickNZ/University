from search import Arc, Graph
from math import sqrt

class LocationGraph(Graph):
    def __init__(self, location, radius, starting_nodes, goal_nodes):
        self.location = location
        self.radius = radius
        self._starting_nodes = starting_nodes
        self.goal_nodes = goal_nodes
    
    def starting_nodes(self):
        return self._starting_nodes
    
    def is_goal(self, node):
        return node in self.goal_nodes # replace this line with a correct code
    
    def outgoing_arcs(self, tail):
        arc_list = []
        for key in self.location:
            cost = self.not_plagarised_calc(self.location.get(tail), self.location.get(key))
            if (cost <= self.radius) and (cost > 0.0):
                arc_list.append(Arc(tail, key, tail + "->" + key, cost))
        return sorted(arc_list, key=lambda x:x.head)
    
    #some vector math (thanks cosc262)
    def not_plagarised_calc(self, x, y):
        z = [y[0] - x[0], y[1] - x[1]] # y - x
        return sqrt(z[0]**2 + z[1]**2) #incase negative


def main():
    graph = LocationGraph(
        location={'SW': (-2, -2),
                'NW': (-2, 2),
                'NE': (2, 2),
                'SE': (2, -2)},
        radius = 5,
        starting_nodes=['NE'],
        goal_nodes={'SW'}
    )

    for arc in graph.outgoing_arcs('NE'):
        print(arc)

    print()

    for arc in graph.outgoing_arcs('NW'):
        print(arc)

    print()

    for arc in graph.outgoing_arcs('SW'):
        print(arc)

    print()


    for arc in graph.outgoing_arcs('SE'):
        print(arc)

if __name__ == "__main__":
    main()
