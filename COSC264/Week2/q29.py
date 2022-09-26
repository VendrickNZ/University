def avg_trials_from_ber(bit_error_probability, packet_length_b):
    pp = per_from_ber(bit_error_probability, packet_length_b)
    return average_trials(pp)

def per_from_ber(bit_error_prob, packet_len_b):
    return 1 - (1 - bit_error_prob)**packet_len_b

def average_trials(p_loss):
    return 1 / (1 - p_loss)


print(f"{avg_trials_from_ber(0.001, 2000):.3f}")