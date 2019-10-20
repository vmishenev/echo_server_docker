#!/usr/bin/env python

import socket
import logging
 
# add filemode="w" to overwrite
logging.basicConfig(filename="/var/log/server.log", level=logging.INFO)

sock = socket.socket()
sock.bind(('', 9091))
sock.listen(1)
conn, addr = sock.accept()

print ('connected:', addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.send("OK:".encode('utf-8') + data)
    logging.info(data)
conn.close()
