def parent_index_7_heap(child_index):
    if child_index == 1:
        return None
    else:
        return ((child_index - 2) // 7) + 1
print(parent_index_7_heap(2))

print(parent_index_7_heap(3))


print(parent_index_7_heap(10))

print(parent_index_7_heap(11))
print(parent_index_7_heap(19))
print(parent_index_7_heap(22))
print(parent_index_7_heap(32))
print(parent_index_7_heap(36))
print(parent_index_7_heap(1115))
print(parent_index_7_heap(1121))
