import requests
import json

expData={"empName":"Arun",
         "password":"Computer",
         "role":"User"}
headersSet={"Content-type":"application/json"}
inputData = json.dumps(expData)
req =requests.post("http://localhost:8080/emp/register",data=inputData,headers=headersSet)
print(req)
print(req.text)