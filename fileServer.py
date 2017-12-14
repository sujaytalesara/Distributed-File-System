
import os
import PortManager


urls = ('/fileserver/(.*)/payload/(.*)','fileServer2',
'/fileserver/(.*)','fileServer')



class fileServer:

     def GET(self,filePath):
          if os.path.isfile(filePath):
               with open(filePath,'r') as file:
                    return file.read()
          else:
               value = (os.path.isfile(filePath)) + "****" + filePath
               return value

class fileServer2:

     def POST(self,filePath,payload):
          if os.path.isfile(filePath):
               with open(filePath,'a') as file:
                    file.write(payload)
                    return 'Done'

if __name__=="__main__":
	app = PortManager.changePort(urls,globals())
	app.run(port=8080)


'''
shelf = shelve.open('word_list.dat')
shelf['foo'] = {'bar':1}
shelf.close()
'''
