from math import *
from search import *
import heapq

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

class LCFSFrontier(Frontier):
    def __init__(self):
        self.container = []
        self.count = 0
    
    def add(self, path):
        total_path_cost = 0
        for arc in path:
            total_path_cost += arc.cost
        heapq.heappush(self.container, (total_path_cost,self.count,path)) #implementation notes good
        self.count += 1
    
    def __iter__(self):
        while self.container:
            yield heapq.heappop(self.container)[-1]
    
    def __next__(self):
        return self

def main():
    graph = ExplicitGraph(nodes=set('ABCD'),
                        edge_list=[('A', 'D', 7), ('A', 'B', 2),
                                    ('B', 'C', 3), ('C', 'D', 1)],
                        starting_nodes=['A'],
                        goal_nodes={'D'})

    solution = next(generic_search(graph, LCFSFrontier()))
    print_actions(solution)

if __name__ == "__main__":
    main()