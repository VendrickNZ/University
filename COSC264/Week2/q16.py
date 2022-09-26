def transmission_delay(packet_length_bytes, rate_bps):
    return (packet_length_bytes * 8) / rate_bps # length of packet in bits / bits per second
print(f"{transmission_delay(1000000, 4000000):.3f}")