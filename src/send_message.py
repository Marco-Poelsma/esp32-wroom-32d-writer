from Message import Message
import socket

def send_message(message: Message, port: int, ip: str):
    sock = socket.socket(socket.AF_INET,
                         socket.SOCK_DGRAM)
    sock.bind((ip, port))

    while True:
        