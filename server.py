#!/usr/bin/python
# coding=utf-8

# This example is in Python 3.5.2 document.
# server.py

import os
import socket
from adapt import input

# HOST = 'localhost'
HOST = socket.gethostname()
PORT = 9999

# 创建 tcp socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)
    print('等待客户端连接...')
    conn, addr = s.accept()
    with conn:
        print('Connected by {}'.format(addr))
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print('Received data 【{}】 from {}'.format(data.decode(),addr))
            string = input('请输入要发送的内容：')
            conn.sendall(string.encode())
            
os.system('pause')
