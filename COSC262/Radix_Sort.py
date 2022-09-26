def radix_sort(numbers, d):
    number_list = []
    current_number = 0
    for i in range(len(numbers)):
        if d == 1:
            current_number = (numbers[i] % 10)
            number_list.append(current_number)
            counting_sort(numbers, lambda x: current_number)
        elif d == 2:
            current_number = (numbers[i] % 100) // 10
            number_list.append(current_number)
        else:
            current_number = (numbers[i] // 10) // 10
            number_list.append(current_number)
    return number_list

def counting_sort(iterable, key):
    positions = key_positions(iterable, key)
    return sorted_array(iterable, key, positions)

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

print(radix_sort([329, 457, 657, 839, 436, 720, 355], 1))
# print(radix_sort([329, 457, 657, 839, 436, 720, 355], 1))
# print(radix_sort([329, 457, 657, 839, 436, 720, 355], 2))
