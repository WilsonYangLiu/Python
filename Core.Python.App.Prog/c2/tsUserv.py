#!/usr/bin/env python
# -*- coding: utf-8 -*-

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSork = socket(AF_INET, SOCK_DGRAM)
udpSerSork.bind(ADDR)

try:
    while True:
        print "waiting for message..."
        data, addr = udpSerSork.recvfrom(BUFSIZ)
        udpSerSork.sendto('[%s] %s' % (ctime(), data), addr)
        print "...received from and returned to: ", addr
except (EOFError, KeyboardInterrupt):
    udpSerSork.close()