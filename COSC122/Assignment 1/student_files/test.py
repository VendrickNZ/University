def weird_algorithm(n):
    n_list = n
    while n != 1:
        if n % 2 == 0:
            n /= 2
            n_list += n
        else:
            n = (n * 3) + 1
            n_list += n

    return n_list
print(weird_algorithm(3))