def connection_setup_delay(cable_length_km, light_speed_kmps, message_length_b, data_rate_bps, processing_time_s):
    L, c, R, M, P = cable_length_km, light_speed_kmps, data_rate_bps, message_length_b, processing_time_s
    processing_delay = P * 4
    propagation_delay = (L * 4)/c
    transmission_delay = (M / R) * 4
    return processing_delay + propagation_delay + transmission_delay 

print(f"{connection_setup_delay(10000, 200000, 4000, 1000000, 0.001)}") #0.2080