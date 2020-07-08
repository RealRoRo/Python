import socket
import pickle

HEADER_SIZE = 10
c = socket.socket()

c.connect(("localhost", 9999))

while True:
    new_msg = True
    msg = b''
    while True:
        short_msg = c.recv(16)
        if new_msg:
            print(f"new messge length:{short_msg[:HEADER_SIZE]}")
            msglen = int(short_msg[:HEADER_SIZE])
            new_msg = False

        msg += short_msg
        if len(msg) - HEADER_SIZE == msglen:
            print("full msg recieved")
            print(msg[HEADER_SIZE:])
            friends = pickle.loads(msg[HEADER_SIZE:])
            print(friends)

            new_msg = True
            msg = b""

