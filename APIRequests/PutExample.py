import requests
import json

body={"invoiceId":3456,"amount":1424,"catagory":"Fever","status":"Raised","employeeId":12}
reqBody = json.dumps(body)
headers={"Content-type":"application/json"}
req=requests.put("http://localhost:8080/emp/12/saveClaim",data=reqBody,headers=headers)
print(req.status_code)
print(req.text)