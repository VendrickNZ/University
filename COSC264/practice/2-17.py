def transmission_delay(packet_length_bytes, rate_mbps):
    rate_bps = rate_mbps * 1000000

    return (packet_length_bytes * 8) / rate_bps
print (f"{transmission_delay(1000000, 4):.3f}")