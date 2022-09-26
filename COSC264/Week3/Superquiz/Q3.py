def destination_address(packet):
    addr = (packet[16] << 24) | (packet[17] << 16) | (packet[18] << 8) | (packet[19])
    dd =  "{}.{}.{}.{}".format(packet[16], packet[17], packet[18], packet[19])
    return (addr, dd)