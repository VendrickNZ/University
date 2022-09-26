def basic_packet_check(packet):
    print(packet[0])
    if len(packet) < 20:
        return 1
    if (packet[0] >> 4) != 4:
        return 2
    if not headerchecksum(packet):
        return 3
    if (packet[2] + packet[3]) != len(packet):
        return 4
    return True

def headerchecksum(packet):
    x = 0
    for pair in range(10):
        offset = (pair * 2)
        x += packet[offset] << 8 | packet[offset + 1]
    x0 = x & 0xFFFF
    x1 = x >> 16
    x = x0 + x1
    return x == 0xFFFF


packet = bytearray([0x45, 0x0, 0x0, 0x1e, 0x4, 0xd2, 0x0, 0x0, 0x40, 0x6, 0x20, 0xb4, 0x12, 0x34, 0x56, 0x78, 0x98, 0x76, 0x54, 0x32, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0])
print(basic_packet_check(packet))




#server test


#import socket

# HOST = '127.0.0.1'
# PORT = 65432

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST, PORT))
#     s.listen()
#     conn, addr = s.accept()
#     with conn:
#         print(f"Connected by {addr}")
#         while True:
#             data = conn.recv(1024)
#             if not data:
#                 break
#             conn.sendall(data)


#client test

# socket.socket()
# HOST = "127.0.0.1"  # The server's hostname or IP address
# PORT = 65432  # The port used by the server

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as s:
#     s.connect((HOST, PORT))
#     s.sendall(b"Hello, world")
#     data = s.recv(1024)

# print(f"Received {data!r}")

print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")