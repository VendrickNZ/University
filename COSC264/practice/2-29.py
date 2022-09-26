def avg_trials_from_ber(bit_error_probability, packet_length_b):
    return 1 - (1 - bit_error_probability)**packet_length_b
print(f"{avg_trials_from_ber(0.0001, 1000):.3f}")