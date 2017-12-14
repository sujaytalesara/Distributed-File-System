import requests as req
url1 = "http://localhost:8081/directoryserver/"
url2 = "http://localhost:8080/fileserver/"
url3 = "http://localhost:8083/lockServer/"
url4 = "http://localhost:8084/authenticationServer/"
filePath = "E:/GitHub/Distributed-File-Server/Hello.txt"
#print(url2 + filePath)


userLevel = input("Do you want to login or sign up --  ")

if userLevel=='login':
     userName = input("Enter Username --  ")
     password = input("Enter Password --  ")
     response = req.get(url4 + userName +"/"+ password)
     if response.text == 'login successful':
          #Directory Server
          fileName = input("Enter File Name : ")
          url1 = url1 + fileName
          response = req.get(url1)
          print("Response is ready: " + response.text)
          filePath = response.text
          #print(type(a))
          print(filePath + "************ FilePath")
          operation = input("Enter the operation: 1.) write 2.) read  --  ")

          if operation =='read':
               url2 = url2 + filePath
               response = req.get(url2)
               print (response)
               print("Response is ready: " + response.text)

          elif operation =='write':
               fileName = input("Enter the file Name to Write :")
               url3 = url3 + fileName
               response_lock = req.get(url3)
               response_lock = response_lock.text
               print("Response is ready: " + response_lock)

               if response_lock =='FileLocked':
                    payload = input("Enter the content you want to append :")
                    url2 = url2 + filePath + '/payload/'+ payload
                    response = req.post(url2)
                    print("Response is ready: " + response.text)
                    response = req.post(url3)
                    print("Response is ready: " + response.text)
               elif response_lock == 'Not':
                    print('File Already locked.')

elif userLevel=='sign up':
     userName = input("Enter your Username")
     password = input("Enter your Password")
     response = req.post(url4 + userName +"/"+ password)
     print(response.text)
else:
     print("Your are not authorised")
    



















#response = req.get(filePath)
#print(filePath + "....")

#print("Response is ready: " + response.text)
#print("Response is ready: " + str(response))
