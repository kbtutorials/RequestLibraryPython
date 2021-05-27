import requests

headerDict={"status":"Approve"}
req=requests.get("http://localhost:8080/Admin/activeClaim",headers=headerDict)
print(req.json())