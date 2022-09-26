import math

def total_number_bits(max_user_data_per_packet_b, overhead_per_packet_b, message_length_b):
    s = max_user_data_per_packet_b
    o = overhead_per_packet_b
    m = message_length_b
    
    return s + o + m if (m % s) != 0 else s + m
print(f"{total_number_bits(1000, 100, 10000):.1f}") # 11000.0
print(f"{total_number_bits(1000, 100, 10001):.1f}") #11101.0
print(f"{total_number_bits(1000, 100, 10999):.1f}") #12099.0