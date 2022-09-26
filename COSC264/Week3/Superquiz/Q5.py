def compose_packet(hdrlen, tosdscp, identification, flags, fragmentoffset, timetolive, protocoltype, sourceaddress, destinationaddress, payload):
    version = 4
    totallength = (hdrlen * 4) + len(payload)
    header = compose_header(version, hdrlen, tosdscp, totallength, identification, flags, fragmentoffset, timetolive, protocoltype, 0x0000 ,sourceaddress, destinationaddress)
    if isinstance(header, int):
        return header
    hdrchecksum = headerchecksum(header)
    header[10], header[11] = hdrchecksum >> 8 & 0xFF, hdrchecksum & 0xFF
    if hdrlen > 5:
        for _ in range(((hdrlen - 5) * 4)):
            header.append(0x0)
    return header + payload

def headerchecksum(packet):
    x = 0
    for pair in range(10):
        if pair == 5:
            continue
        offset = (pair * 2)
        x += packet[offset] << 8 | packet[offset + 1]
    x0 = x & 0xFFFF
    x1 = x >> 16
    x = x0 + x1
    return x ^ 0xFFFF

def compose_header(version, hdrlen, tosdscp, totallength, identification, flags, fragmentoffset, timetolive, protocoltype, headerchecksum, sourceaddress, destinationaddress):
    header = [0, 0, 0, 0, 0]    
    if version != 4:
        return 1
    if (hdrlen < 5) or (bit_counter(hdrlen) > 4):
        return 2
    if (tosdscp < 0) or (bit_counter(tosdscp) > 6):
        return 3
    if (totallength < 0) or (bit_counter(totallength) > 16):
        return 4
    if (identification < 0) or (bit_counter(identification) > 16):
        return 5
    if (flags < 0) or (bit_counter(flags) > 3):
        return 6
    if (fragmentoffset < 0) or (bit_counter(fragmentoffset) > 13):
        return 7
    if (timetolive < 0) or (bit_counter(timetolive) > 8):
        return 8
    if (protocoltype < 0) or (bit_counter(protocoltype) > 8):
        return 9
    if (headerchecksum < 0) or (bit_counter(headerchecksum) > 16):
        return 10
    if (sourceaddress < 0) or (bit_counter(sourceaddress) > 32):
        return 11
    if (destinationaddress < 0) or (bit_counter(destinationaddress) > 32):
        return 12
    
    header[0] = (version << 28) | (hdrlen << 24) | (tosdscp << 18) | (totallength)
    header[1] = (identification << 16) | (flags << 13) | (fragmentoffset)
    header[2] = (timetolive << 24) | (protocoltype << 16) | headerchecksum
    header[3] = sourceaddress
    header[4] = destinationaddress

    byte_array = bytearray()

    for row in header:
        byte_array += (row_to_byte_array(row))
    return byte_array

def bit_counter(integer):
    return len(bin(integer)[2:])

def row_to_byte_array(row):
    return bytearray([(row >> 24) & 0xFF, ((row >> 16) & 0xFF), ((row >> 8) & 0xFF), (row & 0xFF)])

print(compose_packet(16,0,4000,0,63,22,0x06, 2190815565, 3232270145, bytearray([])))
print(compose_packet(4,0,4000,0,63,22,0x06, 2190815565, 3232270145, bytearray([])))
print(compose_packet(5,64,4000,0,63,22,0x06, 2190815565, 3232270145, bytearray([])))