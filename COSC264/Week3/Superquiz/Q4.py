def payload(packet):
    return bytearray(packet[(packet[0] & 0xF)*4:])