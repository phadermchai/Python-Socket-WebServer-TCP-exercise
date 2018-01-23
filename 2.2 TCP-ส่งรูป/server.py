#!/usr/bin/env python

import socket
import os

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 40000  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print 'Connection address:', addr
os.makedirs('image_from_client')
myfile = open('image_from_client\image_from_client.jpg','wb')

while True:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    myfile.write(data)
    break
myfile.close()
print "finished send file"
conn.close()

