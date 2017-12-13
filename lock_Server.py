import os.path
import socket
import select
import sys
from thread import *
import threading
from threading import Thread
import sqlite3




class client_thread(Thread):

       def __init__(self,addr,c):
              Thread.__init__(self)
              self.addr = addr
              self.c = c

       def run(self):
              while True:
                     lock(self.addr,self.c)
              


    
    
        

def Main():
    host = '127.0.0.1'
    port = 6002
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(('',port))
    s.listen(5)

    
    print('server started')
    while(True):
        (c,addr) = s.accept()
        print('client connected ip:'+str(addr))
        Thread = client_thread(addr,c)
        Thread.start()


        
if __name__ == '__main__':    
    Main()