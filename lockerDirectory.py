# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 19:46:21 2017

@author: sujay
"""

import shelve

def updatedDirectory():
      fileName = input('Enter file to be locked')
          
      shelv = shelve.open('locker_Directory.dat')
      shelv[fileName] = {0}
      print(shelv[fileName])
      shelv.close()
     
if __name__=="__main__":
     updatedDirectory()
 
''' 
shelf = shelve.open('word_list.dat')
shelf['foo'] = {'bar':1}
shelf.close()
'''
     