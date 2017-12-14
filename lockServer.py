import PortManager
import shelve


urls = ('/lockServer/(.*)','lockServer')

class lockServer:

     def GET(self,fileName):
         print(fileName + "From Lock server %%%%%%%%%%%%%%%%%")
         shelv = shelve.open("lock_Directory.dat")
         value = shelv[fileName]
         print(value)
         try:
             if value == 0:
                 shelv[fileName] = 1
                 print("**********Success ************")
                 return 'FileLocked'
             elif value == 1:
                 print("************else ************")
                 return 'Not'
         except:
             print('Error while locking')
         finally:
             shelv.close()

     def POST(self,fileName):
          print(fileName)
          shelv = shelve.open("lock_Directory.dat")
          value = shelv[fileName]
          #print(value)
          try:
              if value == 1:
                  shelv[fileName] = 0
                  print("*******Success ***********")
              return 'FileUnLocked'
          except:
              print('Error while locking')
          finally:
              shelv.close()



if __name__=="__main__":
	app = PortManager.changePort(urls,globals())
	app.run(port=8083)
