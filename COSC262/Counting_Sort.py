def counting_sort(a, key):
    n = len(a)
    b = [None] * n
    p = key_positions(a, key)
    for i in a:
        b[p][key(a)] = a
        p[key(a)] = p[key(a)] + 1
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
