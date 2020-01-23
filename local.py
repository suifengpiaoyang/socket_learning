#!/usr/bin/python
#coding=utf-8

# This example is in Python 3.5.2 document.
# local.py

import os
import socket
from adapt import input

# HOST = 'loaclhost'
HOST = socket.gethostname()
PORT = 9999

with socket.socket(socket.AF_INET,socket.SOCK_STREAM)as s:

    s.connect((HOST,PORT))
    string = input('请输入要发送的内容：')
    s.sendall(string.encode())
    data = s.recv(1024)
    print('接收到服务器发来的内容：{}'.format(data.decode()))

os.system('pause')
