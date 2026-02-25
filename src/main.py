from Message import Message
from send_message import send_message

PORT: int = 8080 # Replace with port number
IP: str = '192.168.194.141' # Replace with actual IP

email: str = "FRANSEX"
message_content: str = "BON DIA DEVELOPERS!!!"

message: Message = Message(email, message_content)

send_message(message, PORT, IP)