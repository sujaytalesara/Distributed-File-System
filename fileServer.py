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
          file = str(filename.decode())
          print(file + "****")
          fileSize = str(os.path.getsize('main.py'))
          
          sock.send("Exits" + fileSize )
          #--Receive User response
          userResponce = sock.recv(1024)
          # takes user input
          if userResponce[:2] == 'OK':
               # Open file as read binary
               with open(filename,'rb') as f: 
                    bytesToSend = f.read(1024)
                    while bytesToSend != "":
                         bytesToSend = f.read(1024)
                         sock.send(bytesToSend)
                    
     else:
          sock.send("File Does not Exists --- Error")
          sock.close()
          
def Main():
     host = '127.0.0.1'
     port = 3000
     
     s = socket.socket()
     # binding socket obj with host & port no
     s.bind((host,port))
     # Server starts listening to connnection
     s.listen(5)               
     
     print ("Server Started")
     while True:
          # Connection socket & address
          conn,addr = s.accept()
          print ("client connected ip<:" + str(addr) + ">")
          t = th.Thread(target = retriveFile, args = ('retrive Thread',conn))
          t.start()
     s.close()
     
if __name__ == '__main__':
     Main()
     