import requests
import json
requests.get
req =requests.get("https://api.postalpincode.in/pincode/110001")
response =req.json()

for item in response:
    print(item['Message'])
    print(item['Status'])
    postOffice = item['PostOffice']
    for pDetails in postOffice:
        print(pDetails['Name']+" **"+pDetails['District']+"****"+pDetails['Pincode'])

