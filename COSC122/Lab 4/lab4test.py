def total(data_list):
    if len(data_list) == 0:
        return 0
    else:
        return data_list[0] + total(data_list[1:])

result = total([19])
print(result == 19)