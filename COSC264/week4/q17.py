import math

def last_fragment_size(message_size_bytes, overhead_per_packet_bytes, maximum_n_packet_size_bytes):
    s = message_size_bytes
    o = overhead_per_packet_bytes
    m = maximum_n_packet_size_bytes
    return (s %  (m - o)) + o

print (last_fragment_size(10000, 20, 1500))
print (last_fragment_size(11345, 100, 1000))
print (last_fragment_size(13545, 120, 1500))
print (last_fragment_size(17755, 180, 1500))