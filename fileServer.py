import web
import os

urls = ('/fileserver/(.*)','fileServer')
#web.config.debuug = False

class fileServer:

	def GET(self,filePath):
		
		if os.path.isfile(filePath):
			with open(filePath) as file:
				return file.read()
		else:
			value = (os.path.isfile(filePath)) + "****" + filePath
			return value

	def POST(self,name):
		return "post"

if __name__=="__main__":
	app = web.application(urls,globals())
	app.run()


''' 
shelf = shelve.open('word_list.dat')
shelf['foo'] = {'bar':1}
shelf.close()
'''