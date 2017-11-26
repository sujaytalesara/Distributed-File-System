import requests as req

url = "http://localhost:8080/filepath/"

filePath = input("Enter File Name : ")
url = url + filePath
response = req.get(url)
#print(filePath)
#print(url)
print("Response is ready: " + response.text)
