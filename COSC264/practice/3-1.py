def connection_setup_delay(cable_length_km, light_speed_kmps, message_length_b, data_rate_bps, processing_time_s):
    return (cable_length_km * 4 / light_speed_kmps) + (message_length_b / data_rate_bps) * 4 + (processing_time_s * 4)
print(f"{connection_setup_delay(10000, 200000, 1000, 1000000, 0.001):.4f}") # 0.2080