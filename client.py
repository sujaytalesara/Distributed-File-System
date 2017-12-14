
import requests as req

url1 = "http://localhost:8081/directoryserver/"
url2 = "http://localhost:8080/fileserver/"
url3 = "http://localhost:8083/lockServer/"
filePath = "E:/GitHub/Distributed-File-Server/Hello_World.txt"
print(url2 + filePath)

'''
fileName = input("Enter File Name : ")
url1 = url1 + fileName
response = req.get(url1)
print("Response is ready: " + response.text)
a = response.text
#print(type(a))
print(a)
'''

operation = input("Enter the operation: 1.) write 2.) read  --")

if operation =='read':
     #filePath = input("Enter the file Name to search :")
     url2 = url2 + filePath
     response = req.get(url2)
     print (response)
     print("Response is ready: " + response.text)

elif operation =='write':

     fileName = input("Enter the file Name to Write :")
     url3 = url3 + "fileName/"+ fileName
     response_lock = req.get(url3)
     print("Response is ready: " + response_lock.text)

     if response_lock.text=='FileLocked':
          payload = input("Enter the content you want to append :")
          url2 = url2 + filePath + '/payload/'+ payload
          response = req.post(url2)
          print("Response is ready: " + response.text)
          response = req.post(url3)
          print("Response is ready: " + response.text)
     elif response_lock.text== 'Not':
          print('File Already locked.')





















#response = req.get(filePath)
#print(filePath + "....")

#print("Response is ready: " + response.text)
#print("Response is ready: " + str(response))
