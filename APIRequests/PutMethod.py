import requests
import json
bodyData={"invoiceId":12346,"amount":4913,"catagory":"Fever","status":"Approved","employeeId":44}
headersSet={"Content-type":"application/json"}
jsonData = json.dumps(bodyData)
req=requests.put("http://localhost:8080/emp/12/saveClaim",data=jsonData,headers=headersSet)
print(req)
print(req.text)