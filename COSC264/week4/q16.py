import math

def number_fragments(message_size_bytes, overhead_per_packet_bytes, maximum_N_packet_size_bytes):
    s = message_size_bytes
    o = overhead_per_packet_bytes
    m = maximum_N_packet_size_bytes
    
    return math.ceil(s / (m - o))

print(number_fragments(10000, 20, 1500)) # 12