import requests
import json
req=requests.get("https://api.postalpincode.in/pincode/110001")
response =req.json()
for item in response:
    print(item['Message'])
    print(item['Status'])
    postalArray = item['PostOffice']
    for k in postalArray:
        print(k['Name'])
        print(k['District'])
