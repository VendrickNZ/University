def decodedate(x):
    return ((x & 0xF0000000) >> 28) + 1
print(decodedate(1107298273))