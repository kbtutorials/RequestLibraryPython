import requests
import json
postData={"empName":"Dilip23",
          "password":"Computer",
          "role":"User"}
headers ={"Content-type":"application/json"}
jsonData = json.dumps(postData)
print(jsonData)
req =requests.post("http://localhost:8080/emp/register",data=jsonData,headers =headers)
print(req.status_code)
print(req.text)