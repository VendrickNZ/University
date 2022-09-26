def sorted_array(seq, key, positions):
    n = len(seq)
    b = [None] * n
    p = key_positions(seq, key)
    for i in seq:
        b[p[key(i)]] = i
        p[key(i)] = p[key(i)] + 1
    return b

def key_positions(seq, key):
    k = 0
    for i in range(len(seq)):
        if key(seq[i]) > k:
            k = key(seq[i])
    k += 1
    c = []
    for i in range(k):
        c.append(0)
    for i in range(k):
        c[i] = 0
    for i in seq:
        c[key(i)] = c[key(i)] + 1
    new_sum = 0
    temp = 0
    for i in range(k):
        temp = c[i]
        c[i] = new_sum
        new_sum = new_sum + temp
    return c







print(sorted_array([3, 1, 2], lambda x: x, [0, 0, 1, 2]))
print(sorted_array([3, 2, 2, 1, 2], lambda x: x, [0, 0, 1, 4]))
print(sorted_array([100], lambda x: x, [0]*101))
"""Counting Sort"""
import operator

def counting_sort(iterable, key):
    positions = key_positions(iterable, key)
    return sorted_array(iterable, key, positions)
    
objects = [("a", 88), ("b", 17), ("c", 17), ("d", 7)]

key = operator.itemgetter(1)
print(", ".join(object[0] for object in counting_sort(objects, key)))
