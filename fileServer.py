# -*- coding: utf-8 -*-
"""
@author: sujay
description : Distributed file system
"""

import web

urls = ('/(.+)','Index')

class Index:
	def GET(self,name=None):
		return ("Hello World !" + name)
	def POST(self,name):
		return "post"

if __name__=="__main__":
	app = web.application(urls,globals())
	app.run()
