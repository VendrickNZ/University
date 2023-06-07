from search import *
import copy
from collections import deque

BLANK = ' '

class SlidingPuzzleGraph(Graph):
    """Objects of this type represent (n squared minus one)-puzzles.
    """

    def __init__(self, starting_state):
        self.starting_state = starting_state

    def outgoing_arcs(self, state):
        """Given a puzzle state (node) returns a list of arcs. Each arc
        represents a possible action (move) and the resulting state."""
        
        n = len(state) # the size of the puzzle
        i, j = 1, 1
        # Find i and j such that state[i][j] == BLANK
        for x in range(n):
            for y in range(n):
                if state[x][y] == BLANK:
                    i, j = x, y
        arcs = []
        if i > 0:
            action = "Move {} down".format(state[i-1][j]) # or blank goes up
            new_state = copy.deepcopy(state) 
            new_state[i][j], new_state[i-1][j] = new_state[i-1][j], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        if i < n - 1:
            action = "Move {} up".format(state[i+1][j]) # or blank goes down
            new_state = copy.deepcopy(state) 
            new_state[i][j], new_state[i+1][j] = new_state[i+1][j], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        if j > 0:
            action = "Move {} right".format(state[i][j-1]) # or blank goes left
            new_state = copy.deepcopy(state) 
            new_state[i][j], new_state[i][j-1] = new_state[i][j-1], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        if j < n - 1:
            action = "Move {} left".format(state[i][j+1]) # or blank goes left
            new_state = copy.deepcopy(state) 
            new_state[i][j], new_state[i][j+1] = new_state[i][j+1], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        return arcs

    def starting_nodes(self):
        return [self.starting_state]
    
    def is_goal(self, state):
        """Returns true if the given state is the goal state, False
        otherwise. There is only one goal state in this problem."""
        
        n = len(state)
        area = n*n
        if state[0][0] != BLANK:
            return False
        for i in range(1, area):
            if state[i//n][i%n] != i:
                return False
        return True

        # COMPLETE
        

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
    
if __name__ == "__main__":
    graph = SlidingPuzzleGraph([[1, 2, 5],
                            [3, 4, 8],
                            [6, 7, ' ']])

    solutions = generic_search(graph, BFSFrontier())
    print_actions(next(solutions))

    
    graph = SlidingPuzzleGraph([[3,' '],
                                [1, 2]])

    solutions = generic_search(graph, BFSFrontier())
    print_actions(next(solutions))

    
    graph = SlidingPuzzleGraph([[1, ' ', 2],
                                [6,  4,  3],
                                [7,  8,  5]])

    solutions = generic_search(graph, BFSFrontier())
    print_actions(next(solutions))