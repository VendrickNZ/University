def message_delay(conn_setup_time_s, cable_length_km, light_speed_kmps, message_length_b, data_rate_bps):
    progagation_delay = cable_length_km/light_speed_kmps
    transmission_delay = message_length_b/data_rate_bps
    return ((progagation_delay*2) + transmission_delay) + conn_setup_time_s
print(f"{message_delay(0.2, 10000, 200000, 1000000000, 1000000):.3f}") #0.460