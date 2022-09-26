def convert(x, base):
    if not isinstance(x, int):
        return -1
    if not isinstance(base, int):
        return -2
    if x < 0:
        return -3    
    
    num = []
    
    while x // base != 0:
        num.append(x % base)
        x //= base
    num.append(x % base)
    num.reverse()
    return num