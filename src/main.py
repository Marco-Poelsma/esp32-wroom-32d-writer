from Message import Message
from send_message import send_message

PORT: int = 0 # Replace with port number
IP: str = 'target_ip' # Replace with actual IP

email: str = "your_email@example.com"
message_content: str = "Put your message content here."

message: Message = Message(email, message_content)

send_message(message, PORT, IP)