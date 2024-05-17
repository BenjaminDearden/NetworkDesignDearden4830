# github repository: https://github.com/BenjaminDearden/NetworkDesignDearden4830
import socket

#Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Bind the socket to port and address

server_address = (socket.gethostbyname(socket.gethostname()), 12000)

sock.bind(server_address)

while True:
    print("\nWaiting to receive message")
    data, address = sock.recvfrom(4096)
    
    print("Received %s bytes from %s" % (len(data), address))
    print("Data: %s" % data)
    
    if data:
        sent = sock.sendto(data, address)
        print("Sent %s bytes back to %s" % (sent, address))
        