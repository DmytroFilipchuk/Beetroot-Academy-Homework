"""
Task 2

Extend the echo server, which returns to client the data, encrypted using the Caesar cipher algorithm 
by a specific key obtained from the client.

"""

import string
import socket

"""CLASS FOR CAESAR ENCRYPTION"""


class Caesar:

    default_alphabets = (string.ascii_lowercase, string.ascii_uppercase, string.punctuation)

    def __init__(self):
        pass

    def shift_alphabet(self, shift, alphabet="".join(default_alphabets)):
        return alphabet[shift:] + alphabet[:shift]

    def translation_table(self, alphabet, shifted_alphabet):
        return str.maketrans(alphabet, shifted_alphabet)

    def caesar_it(self, text, shift, alphabet="".join(default_alphabets)):
        shifted_alphabet = self.shift_alphabet(shift, alphabet)

        return text.translate(self.translation_table(alphabet, shifted_alphabet))


"""SERVER CODE"""

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("127.0.0.1", 12345))

while True:
    data, address = server.recvfrom(1024)

    message = "Enter a key: "
    server.sendto(message.encode("utf-8"), address)

    key, address = server.recvfrom(1024)
    encryption = Caesar().caesar_it(data.decode("utf-8"), int(key))
    server.sendto(encryption.encode("utf-8"), address)

"""CLIENT CODE"""

server_data = ("127.0.0.1", 12345)
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

msg = input("Enter string: ")
client.sendto(msg.encode("utf-8"), server_data)
data, address = client.recvfrom(1024)
print(f"Server: {data.decode('utf-8')}")

key = str(input(""))
client.sendto(key.encode("utf-8"), server_data)
data, address = client.recvfrom(1024)
print(f"Server: {data.decode('utf-8')}")

client.close()
