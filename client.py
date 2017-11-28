import requests as req

#url = "http://localhost:8080/fileserver/"
url = "http://localhost:8081/directoryserver/"

filePath = input("Enter File Name : ")

url = url + filePath
response = req.get(url)
#response = req.get(filePath)

print(filePath + "....")
print("Response is ready: " + response.text)
print("Response is ready: " + str(response))
