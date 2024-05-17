#github repository: https://github.com/BenjaminDearden/NetworkDesignDearden4830
import socket

#create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = (socket.gethostbyname(socket.gethostname()), 12000)
message = b'HELLO'

try:
    #send data
    print("Sending %s" % message)
    sent = sock.sendto(message, server_address)
    
    #receive response
    print("Waiting to receive")
    data, server = sock.recvfrom(4096)
    print("Received %s" % data)
    
finally:
    print("Closing socket")
    sock.close()