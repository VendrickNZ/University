def message_delay(conn_setup_time_s, cable_length_km, light_speed_kmps, message_length_b, data_rate_bps):
    return (cable_length_km*2 / light_speed_kmps) + (message_length_b / data_rate_bps) + conn_setup_time_s

print(f"{message_delay(0.305, 15000, 200000, 5000, 1000000):.3f}")