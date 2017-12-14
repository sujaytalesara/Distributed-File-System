import PortManager
import shelve

urls = ('/authenticationServer/(.*)/(.*)','authenticationServer')


class authenticationServer:
     
     def GET(self,userName,password):
          objShelve = shelve.open("authenticationDirectory.dat")
          val = objShelve[userName]
          
          if objShelve[userName] == password:
               print(val + "............"+password)
               return "login successful"
          else:
               return "wrong credentials"
          
          
          
     def POST(self,userName,password):
          objShelve = shelve.open("authenticationDirectory.dat")
          key = list(objShelve.keys())
          
          if userName in key:
               return "Username already present"
          else:
               objShelve[userName] = password
               return userName + "successfully registered"
               
          
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     if __name__=="__main__":
          app = PortManager.changePort(urls,globals())
          app.run(port=8084)