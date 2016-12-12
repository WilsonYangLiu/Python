#!/usr/bin/env python
# -*- coding: utf-8 -*-

from socket import *

HOST = '104.236.139.36'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

while True:
    tcpCliSork = socket(AF_INET, SOCK_STREAM)
    tcpCliSork.connect(ADDR)
    data = raw_input("> ")
    if not data:
        break
    tcpCliSork.send("%s\r\n" % data)
    data = tcpCliSork.recv(BUFSIZ)
    if not data:
        break
    print data
    tcpCliSork.close()
