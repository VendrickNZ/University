def transmission_delay(packet_length_bytes, rate_mbps):
    packet_length_bits = packet_length_bytes * 8
    rate_bps = rate_mbps * 1000000
    return packet_length_bits / rate_bps #returns in seconds

print (f"{transmission_delay(1000, 10000)}")