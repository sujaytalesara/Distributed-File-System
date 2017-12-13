import os.path
import socket
import select
import sys
from thread import *
from threading import Thread
import sqlite3

class client_thread(Thread):

       def __init__(self,addr,c):
              Thread.__init__(self)
              self.addr = addr
              self.c = c

       def run(self):
              while True:
                     auth_server(self.addr,self.c)


def auth_server(name,c):
       inp = c.recv(2048)
       print 'started'
       username = c.recv(2048)
       print 'us'
       password = c.recv(2048)
       print 'pw'
       
       print(username, password, inp)
       conn = sqlite3.connect('authen.db')
       print "Opened database successfully";
       val = ''
       p= ''
       i=0
       print '1'
       if inp=='1':
              cursor = conn.execute("SELECT password from data WHERE username = (?)", (username,))
              for row in cursor:                     
                     p = row[0]
              if p == password:
                     val = 'true'
              else:
                     val = 'false'
       elif inp == '2':
              cursor = conn.execute("SELECT username from data")
              for row in cursor:                     
                     u = row[0]
                     if u == username:
                            i=1
              if i!= 0:
                     val = 'exists'
              else:                            
                     cursor = conn.execute("INSERT INTO data VALUES (?, ?)", (username, password))
                     conn.commit()
                     val = 'true'
       else:
              val = 'exit'
       c.send(val.encode())
    





def Main():
    host = '127.0.0.1'
    port = 5009
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