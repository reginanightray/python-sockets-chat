import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 11719))
clients = []
print('Start Server')

while True:
    try:
        data, address = sock.recvfrom(1024)
        if address not in clients:
            clients.append(address)
            print('client connected from '+address[0]+':'+str(address[1]))
        print(address[0]+':'+str(address[1]), data)
        for client in clients:
            sock.sendto(data, client)
    except socket.error:
        pass