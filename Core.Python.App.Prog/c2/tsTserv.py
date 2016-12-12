#!/usr/bin/env python
# -*- coding: utf-8 -*-

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSork = socket(AF_INET, SOCK_STREAM)
tcpSerSork.bind(ADDR)
tcpSerSork.listen(5)

try:
    while True:
        print "waiting for connection..."
        tcpCliSork, addr = tcpSerSork.accept()
        print "...connected from: ", addr
    
        while True:
            data = tcpCliSork.recv(BUFSIZ)
            if not data:
                break
            tcpCliSork.send('[%s] %s' % (ctime(), data))
    
        tcpCliSork.close()
except (EOFError, KeyboardInterrupt):
    tcpSerSork.close()

