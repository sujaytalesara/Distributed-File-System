# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 17:09:30 2017

@author: sujay
"""

import web
import shelve

urls = ('/directoryserver/(.*)','directoryServer')
#web.config.debuug = False

class directoryServer:

	def GET(self,fileName):
         
         try:
             
              value = ""
              objShelve = shelve.open("Directory_names.dat")
              keys = list(objShelve.key())
              print(keys + "1..")
     
              if fileName == "*" :
                   value = keys
                   print(value + "2..")
              elif fileName in keys:
                   value = list(objShelve["fileName"])
                   print(value + "3...")
              else:
                   value = "Nothing Found " +  list(objShelve.keys())
                   print(value + "4...")
              
         finally:
              objShelve.close()
              
              return value
                         
               
	def POST(self,name):
		return "post"

if __name__=="__main__":
	app = web.application(urls,globals())
	app.run()
