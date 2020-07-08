import socket
import time
import pickle

HEADER_SIZE = 10

s = socket.socket()
print("socket created")
s.bind(("localhost", 9999))
s.listen(3)
print("Waiting for connections")
while True:
    c, addr = s.accept()
    print("Connected with ", addr)

    friends =  ["Sandeep", "Dino", "Amal", "Amal", "Terin", "Francis", "Abay", "Adarsh", "Ajith", "Akhil", "Hridik"]
    msg = pickle.dumps(friends)


    msg = bytes(f"{len(msg):<{HEADER_SIZE}}", "utf-8") + msg

    c.send(msg)




