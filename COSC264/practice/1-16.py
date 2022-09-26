def decodedate(n):
    month = (n >> 28) + 1
    day = ((n & 0xF800000) >> 23) + 1
    year = (n & 0x3FFFFF)

    return f"{day}.{month}.{year}"
print(decodedate(1107298273))