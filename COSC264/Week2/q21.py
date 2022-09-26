def queueing_delay(rate_mbps, num_packets, packet_length_bytes):
    packet_length_bits = packet_length_bytes * 8
    rate_bps = (rate_mbps * 10**6)
    return (packet_length_bits / rate_bps) * num_packets

print(f"{queueing_delay(100, 20, 1500)}")

L = 1500 * 8
R = 100000000
N = 20

print((L/R)*N)