from Message import Message
import socket

def send_message(message: Message, port: int, ip: str):
    # We define the socket to use internet and UDP
    sock = socket.socket(socket.AF_INET,
                         socket.SOCK_DGRAM)
    
    # The data we will send ca be found here
    data = str(f"{message.email} diu {message.content}").encode('utf-8')
    
    # Now we can send the data over UDP.
    sock.sendto(data, (ip, port))

    sock.close()

    pass
