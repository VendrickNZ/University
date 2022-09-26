def packet_transfer_time(link_length_km, light_speed_kmps, processing_delay_s, data_rate_bps, max_user_data_per_packet_b, overhead_per_packet_b):
    l = link_length_km
    c = light_speed_kmps
    p = processing_delay_s
    r = data_rate_bps
    s = max_user_data_per_packet_b
    o = overhead_per_packet_b

    propagation_delay = l/c
    transmission_delay = (s + o) / r

    return (propagation_delay + transmission_delay + p) * 2

print( packet_transfer_time (15000, 250000, 0.001, 1000000, 4192, 100))