import web
import os

urls = ('/filepath/(.*)','fileServer')
#web.config.debug = False

class fileServer:

	def GET(self,filePath):
		if os.path.isfile(filePath):
			with open(filePath) as file:
				return file.read()
		else:
			value = "File not Found at --- "(os.path.isfile(filePath))
#			print(value + "**************")
			return value

	def POST(self,name):
		return "post"

if __name__=="__main__":
	app = web.application(urls,globals())
	app.run()