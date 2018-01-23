#!/usr/bin/env python

import socket
import os


TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 40000
File = "test.jpg"
bytes1 = open(File,'rb').read(BUFFER_SIZE)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(bytes1)
s.close()
