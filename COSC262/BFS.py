from collections import deque

def bfs_tree(adj_list, start):
    n = len(adj_list)
    state = []
    parent_array = []
    for i in range(n):
        state.append("U")
        parent_array.append(None)
    bfs_deque = deque()

    state[start] = "D"
    bfs_deque.append(start)

    return bfs_loop(adj_list, bfs_deque, state, parent_array)


def bfs_loop(adj_list, bfs_deque, state, parent_array):
    while bfs_deque:
        u = bfs_deque.pop()
        for v in adj_list[u]:
            neighbour = v[0]
            if state[neighbour] == "U":
                state[neighbour] = "D"
                parent_array[neighbour] = u
                bfs_deque.appendleft(neighbour)
            state[u] = "P"
    return parent_array
