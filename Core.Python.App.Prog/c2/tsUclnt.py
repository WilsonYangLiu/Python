#!/usr/bin/env python
# -*- coding: utf-8 -*-

from socket import *

HOST = '104.236.139.36'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSork = socket(AF_INET, SOCK_DGRAM)

while True:
    data = raw_input("> ")
    if not data:
        break
    udpSerSork.sendto(data, ADDR)
    data, ADDR = udpSerSork.recvfrom(BUFSIZ)
    if not data:
        break
    print data
    
udpSerSork.close()