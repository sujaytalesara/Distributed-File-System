# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 15:05:12 2017

@author: sujay
"""

import socket
def Main():
     host = '127.0.0.1'
     port = 3000
     
     s = socket.socket()
     s.connect((host,port))
     # Input filename from client
     fileName = input('Filename? ->-')
     if fileName != 'q':
          print(fileName)
          s.send(fileName.encode())
          data = s.recv(1024)
          if data[:6] == 'EXISTS':
               # save file size from 6th character
               fileSize = long(data[6:])
               message = input("File Exists," + str(fileSize) +\
                               "Bytes,download? (Y/N)? ->")
               if message == 'Y':
                    s.send('OK')
                    # Write binary & saves filename with keyword New_
                    f = open('new_' + fileName,'wb')
                    data = s.recv(1024)
                    totalReceive = len(data)
                    f.write(data)
                    while totalReceive < fileSize:
                         data = s.recv(1024)
                         totalReceive += len(data)
                         f.write(data)
                         print("{0:2f}".format(totalReceive/float(fileSize)) * 100 + 
                               "% Done")
                    print("Download Complete")
          else:
               print("File does not exists")
          s.close()
          
if __name__ == '__main__':
     Main()
               