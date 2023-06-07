from search import *
from itertools import dropwhile
from collections import deque
class FunkyNumericGraph(Graph):
    """A graph where nodes are numbers. A number n leads to n-1 and
    n+2. Nodes that are divisible by 10 are goal nodes."""
    
    def __init__(self, starting_number):
        self.starting_number = starting_number

    def outgoing_arcs(self, tail_node):
        """Takes a node (which is an integer in this problem) and returns
        outgoing arcs (always two arcs in this problem)"""
        return [Arc(tail_node, tail_node-1, action="1down", cost=1),
                Arc(tail_node, tail_node+2, action="2up", cost=1)]
        
    def starting_nodes(self):
        """Returns a sequence (list) of starting nodes. In this problem
        the seqence always has one element."""
        return [self.starting_number]

    def is_goal(self, node):
        """Determine whether a given node (integer) is a goal."""
        return node % 10 == 0

class BFSFrontier(Frontier):
    """Implements a frontier container appropriate for depth-first
    search."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.container = []

    def add(self, path):
        self.container.append(path) # FIX THIS (store the given path)

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self
        
    def __next__(self):
        self.container = deque(self.container)
        if len(self.container) > 0:
            return self.container.popleft()# FIX THIS (return something instead)
        else:
            raise StopIteration   # don't change this one

graph = FunkyNumericGraph(4)
for node in graph.starting_nodes():
    print(node)

graph = FunkyNumericGraph(4)
for arc in graph.outgoing_arcs(7):
    print(arc)

graph = FunkyNumericGraph(3)
solutions = generic_search(graph, BFSFrontier())
print_actions(next(solutions))
print()
print_actions(next(solutions))


graph = FunkyNumericGraph(3)
solutions = generic_search(graph, BFSFrontier())
print_actions(next(dropwhile(lambda path: path[-1].head <= 10, solutions)))