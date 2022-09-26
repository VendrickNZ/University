def total_time(cable_length_km, packet_length_b):
    light_speed = 200000
    data_rate_bps = 10000000000
    delay = cable_length_km/light_speed
    delay2 = packet_length_b / data_rate_bps
    return (delay + delay2) * 1000
print(f"{total_time(10000, 8000):.4f}")