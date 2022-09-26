import socket
import sys

HOST = sys.argv[0]
PORT_1 = sys.argv[1]
PORT_2 = sys.argv[2]
PORT_3 = sys.argv[3]

if (PORT_1 != PORT_2) and (PORT_1 != PORT_3) and (PORT_2 != PORT_3):
    if not ((PORT_1 in range(1024, 64000)) and (PORT_2 in range(1024, 64000)) and (PORT_3 in range(1024, 64000))):
        print("ERROR: PORT NUMBERS OUT OF RANGE")
        exit(0)
else:
    print("ERROR: PORT NUMBERS ARE NOT DIFFERENT")
    exit(0)


def main():
    sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    sockfd.bind((HOST, PORT))

if __name__ == "__main__":
    main()

print(len(""))