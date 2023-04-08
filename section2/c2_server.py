import socket

UDP_IP = "0.0.0.0"
UDP_PORT = 3141

sock = socket.socket(
    socket.AF_INET, # Internet
    socket.SOCK_DGRAM # UDP
) 
sock.bind((UDP_IP, UDP_PORT))

print("Listening for responses from bots.")
bots = set()

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    if "ip address:" in str(data):
        ip = data.decode()
        bots.add(ip[ip.index(":")+1:])
        print(bots)