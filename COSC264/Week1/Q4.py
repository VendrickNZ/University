from Q3 import *
def hexstring(x):
    if not isinstance(x, int):
        return -1
    if x < 0:
        return -2
    return str(hex(x)).upper().replace('X', 'x')
    


print(hexstring(1234))