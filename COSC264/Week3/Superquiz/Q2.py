def basic_packet_check(packet):
    if len(packet) < 20:
        return 1
    if (packet[0] >> 4) != 4:
        return 2
    if not headerchecksum(packet):
        return 3
    if (packet[2] + packet[3]) != len(packet):
        return 4
    return True

def headerchecksum(packet):
    x = 0
    for pair in range(10):
        offset = (pair * 2)
        x += packet[offset] << 8 | packet[offset + 1]
    x0 = x & 0xFFFF
    x1 = x >> 16
    x = x0 + x1
    return x == 0xFFFF