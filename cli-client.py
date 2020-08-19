import socket
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
if (len(sys.argv)-1 != 2):
    print('Usage: cli-client.py [NAME] [MESSAGE]')
    sys.exit()

name = sys.argv[1]
message = sys.argv[2]
networkMessage = name + ':' + message
s.sendto(networkMessage.encode(), ('127.0.0.1', 11719))
print(networkMessage)
