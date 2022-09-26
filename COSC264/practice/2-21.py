def queueing_delay(rate_bps, num_packets, packet_length_b):
    delay = packet_length_b/rate_bps
    return delay * num_packets

print (f"{queueing_delay(1000000, 7, 10000):.3f}")