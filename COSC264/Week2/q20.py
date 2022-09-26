def total_time(cable_length_km, packet_length_b):
    speed_of_light = 200000 #two hundred thousand km/s through cable
    rate_gbps = 10
    rate_mbps = rate_gbps * 1000
    rate_bps = rate_mbps * 1000000
    
    transmission_delay = packet_length_b / rate_bps
    propagation_delay = cable_length_km / speed_of_light
    
    return (propagation_delay + transmission_delay) * 1000 #in milliseconds


print(f"{total_time(10000, 8000):.4f}")