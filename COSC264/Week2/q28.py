import numpy


def per_from_ber(bit_error_prob, packet_len_b):
    return 1 - (1 - bit_error_prob)**packet_len_b
print(f"{per_from_ber(0.0001, 1000):.3f}")