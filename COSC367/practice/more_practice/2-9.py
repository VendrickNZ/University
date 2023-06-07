from itertools import count
from search import *
from math import sqrt
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


class LCFSFrontier:
    def __init__(self):
        self.container = []
        self.count = 0
    
    def add(self, path):
        """Adds a new path to the frontier. A path is a sequence (tuple) of
        Arc objects. You should override this method.
        """
        total_path_cost = 0
        for arc in path:
            total_path_cost += arc.cost
        heapq.heappush(self.container, (total_path_cost, self.count, path))
        self.count += 1
        
    def __iter__(self):
        """We don't need a separate iterator object. Just return self. You
        don't need to change this method."""
        while self.container:
            yield heapq.heappop(self.container)[-1]

    
    @abstractmethod
    def __next__(self):

        """Selects, removes, and returns a path on the frontier if there is
        any.Recall that a path is a sequence (tuple) of Arc
        objects. Override this method to achieve a desired search
        strategy. If there nothing to return this should raise a
        StopIteration exception.
        """
        return self

frontier = LCFSFrontier()
frontier.add((Arc(None, None, None, 17),))
frontier.add((Arc(None, None, None, 11), Arc(None, None, None, 4)))
frontier.add((Arc(None, None, None, 7), Arc(None, None, None, 8)))

for path in frontier:
    print(path)