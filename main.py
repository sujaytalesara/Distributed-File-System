# -*- coding: utf-8 -*-
"""
@author: sujay
description : Distributed file system
"""

import socket
import threading as th
import os

def retriveFile(name,sock):
     filename = sock.recv(1024)
     if os.path.isfile(filename):
          sock.send("Exits" + str(os.path.getsize(filename)))
          userResponce = sock.recv(1024)
          if userResponce[:2] == 'OK':
               with open(filename,'rb') as f:
                    bytesToSend = f.read(1024)
                    sock.send(bytesToSend)
     else:
          sock.send("Error")
          sock.close()
          
def Main():
     host = '127.0.0.1'
     port = 5000
     
     s = socket.socket()
     s.bind((host,port))
     s.listen(5)               
     
     print ("Server Started")
     while True:
          c,addr = s.accept()
          print ("client connected ip<:" + str(addr) + ">")
          t = th.Thread(target = retriveFile, args = ('retrive Thread',c))
          t.start()
     s.close()
     
if __name__ == '_main_':
     Main()
     