def encodedate(day, month, year):

    if day < 1 or day > 31 or month < 1 or month > 12:
        return -1

    x = 0
    x |= (month - 1) << 28
    x |= (day - 1) << 23
    x |= year
    
    return x
print(encodedate(5,5,2017))