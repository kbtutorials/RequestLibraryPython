import requests
import json
headerDict={"status":"Approve"}
req =requests.get("http://localhost:8080/Admin/activeClaim",headers=headerDict)
print(req.json())

response = req.json()

for item in response:
    print(item['order_id'])
    print(item['invoiceId'])
    print(item['invoicedate'])
    print(item['amount'])