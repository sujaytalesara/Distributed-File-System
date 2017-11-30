# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 17:09:30 2017
@author: sujay
"""

import web
import PortManager
import shelve

urls = ('/directoryserver/(.*)','directoryServer')
#web.config.debuug = False

class directoryServer:

	def GET(self,fileName):

		try:
			value = ""
			objShelve = shelve.open("Directory_names.dat")
			keys = list(objShelve.keys())

			if fileName == "*":
				 for items in keys:
					 value = value + "\n" + items
			elif fileName in keys:
			#	print(type(objShelve["fileName"]))
				value = objShelve[fileName]
			else:
				 value = "Nothing Found "
		except KeyError :
			print("Error in Keyss")
		except:
			print("Something Else")

		finally:
			objShelve.close()
		return value


if __name__=="__main__":
	app = PortManager.changePort(urls,globals())
	app.run(port=8081)
