def total_transfer_time(link_length_km, light_speed_kmps, processing_delay_s, data_rate_bps, max_user_data_per_packet_b, overhead_per_packet_b, message_length_b):
    l = link_length_km
    c = light_speed_kmps
    p = processing_delay_s
    r = data_rate_bps
    s = max_user_data_per_packet_b
    o = overhead_per_packet_b
    m = message_length_b

    
    propagation_delay = l/c
    transmission_delay = (s + o) / r

    return ((propagation_delay + transmission_delay + p) * 2) + (transmission_delay) * ((m / s) - 1)

print(total_transfer_time (10000, 200000, 0.001, 1000000, 1000, 100, 1000000000))