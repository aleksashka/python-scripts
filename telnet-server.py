#!/usr/bin/env python
'''A simple telnet server that returns to client it's address 
and closes the session

This code is based on how-to:
http://www.binarytides.com/python-socket-server-code-example/

Additional links:
http://www.binarytides.com/python-socket-programming-tutorial/
https://pymotw.com/2/socket/tcp.html
'''

import socket
import sys
from thread import *
 
HOST = ''
PORT = 2323
 
# Function for handling connections. This will be used to create threads
def clientthread(conn,addr):
    conn.send('Your address is: ' + addr[0] + '\n')
    #conn.send('Your port is: ' + str(addr[1]) + '\n')
    conn.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    sys.stderr.write('Bind failed. Error Code: ' + str(msg[0]) + '. Error Message: ' + msg[1] + '.\n')
    sys.exit()
s.listen(10)
try:
    while 1:
        conn, addr = s.accept()
        # start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
        start_new_thread(clientthread ,(conn,addr))
except KeyboardInterrupt:
    print ' Caught a keyboard interrupt. Exiting...'
finally:
    s.close()
